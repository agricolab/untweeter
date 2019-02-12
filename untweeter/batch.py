#!/usr/bin/env python
import time
import json
import twitter
import os
import argparse
from .ini import Ini
from .api import open_api
# %%

def read_likejs(path=None):
    if path is None:
        path = os.path.split(__file__)[0]
        path = os.path.join(path, '../../like.js')

    with open(path) as f:
        lines = f.readlines()
    s = []
    for lix, lin in enumerate(lines):
        if lix == 0:
            s.append('{')
        else:
            s.append(lin.strip())
    s[-1] = '}'
    faves = [json.loads(f) for f in ''.join(s).split(',')]
    fave_ids = [int(fave['like']['tweetId']) for fave in faves]
    return fave_ids


def unfave_old_faves(api, ini, args):

    print(f'Planning to delete {args.delete} old faves')
    fave_ids = ini.get_old_faves(count=args.delete)
    if fave_ids is None:
        print('Nothing left to delete')
        return

    request_count = 0
    for tweet_id in reversed(fave_ids):
        try:
            request_count += 1
            print ('Deleting like #', request_count, tweet_id, end='')
            if args.dry:
                print('...dry run')
                continue
            api.CreateFavorite(status_id=tweet_id)
            print('...liked...', end='')
            api.DestroyFavorite(status_id=tweet_id)
            print('...unliked!')

            ini.remove_old_fave(tweet_id)

            time.sleep(0.1)
        except twitter.TwitterError as err:
            if 'No status found with that ID.' in err.message[0]['message']:
                print('...not found')
            else:
                print("failed with: %s\n" % err.message)


def main():
    'entry point for python -m batch-untweeter'
    parser = argparse.ArgumentParser(description='Configurate execution')
    parser.add_argument('--dry', action="store_true",
                        help='perform a dry run without any actual deletion')

    parser.add_argument('--path', help='path to your like.js file')
    parser.add_argument('--delete', type=int, default=0,
                        help='number of old faves to undo')
    args = parser.parse_args()
    args.delete = abs(args.delete)

    ini = Ini()
    keys = ini.get_keys()
    api = open_api(keys)

    if args.path:
        print(f'Reading old likes from {args.path}')
        fave_ids = read_likejs(args.path)
        ini.set_old_faves(fave_ids)

    unfave_old_faves(api, ini, args)


if __name__ == "__main__":
    main()
