#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
from .api import open_api
from .ini import Ini
from .untweeter import delete, unlike
from untweeter import cfg

#%%
def main():
    "entry point for python -m untweeter"
    parser = argparse.ArgumentParser(description="Configurate execution")
    parser.add_argument(
        "--dry",
        action="store_true",
        help="perform a dry run without any actual deletion",
    )

    parser.add_argument(
        "--list", action="store_true", help="print the current configuration"
    )

    parser.add_argument("--tweet-limit", type=int, help="set the limit for tweets")
    parser.add_argument("--fave-limit", type=int, help="set the limit for faves")

    parser.add_argument(
        "--ask-for-keys", action="store_true", help="ask interactively for keys"
    )

    args = parser.parse_args()
    if args.list:
        for key in cfg.config.keys():
            print(f"[{key}]")
            for k, v in cfg.config[key].items():
                print(f"{k}: {v}")

        quit()

    if args.ask_for_keys:
        cfg.ask_for_keys()
    if args.tweet_limit:
        cfg.set_tweet_limit(args.tweet_limit)
    if args.fave_limit:
        cfg.set_fave_limit(args.tweet_limit)
    keys = cfg.get_keys()
    restrict_tweets, restrict_faves = cfg.get_limits()

    api = open_api(keys)

    print("Limiting tweets to max:{0:4d}".format(restrict_tweets))
    print("Limiting faves to max:{0:5d}".format(restrict_faves))

    delete(api, restrict_tweets, args)
    unlike(api, restrict_faves, args)


if __name__ == "__main__":
    main()
