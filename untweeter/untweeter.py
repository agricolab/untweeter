import time
import twitter
# %%
def delete(api, restrict=100, args=None):
    tweets = api.GetUserTimeline(count=200,
                                 include_rts=True, exclude_replies=False)
    print('You have {0:4d} tweets'.format(len(tweets)))

    if len(tweets)>restrict:
        marks = tweets[restrict:]
        print('Attempt to delete {0:4d} tweets'.format(len(marks)))
        if args.dry:
            print('Dry Run - abort deletion')
            return
        request_count = 0
        for tweet in reversed(marks):
            try:
                print ('Deleting tweet#', request_count, tweet.id, end='')
                api.DestroyStatus(status_id=tweet.id)
                print('...deleted!')
                time.sleep(0.1)
                request_count += 1
            except twitter.TwitterError as err:
                if 'No status found with that ID.' in err.message[0]['message']:
                    print('...not found')
                else:
                    print("failed with: %s\n" % err.message)
    else:
        print('No need to delete any tweets')

def unlike(api, restrict=100, args=None):
    faves = api.GetFavorites(count=200)
    print('You have {0:4d} faves'.format(len(faves)))
    if len(faves)>restrict:
        marks = faves[restrict:]
        print('Attempt to unfave {0:4d} tweets'.format(len(marks)))
        if args.dry:
            print('Dry Run - abort unfaving')
            return
        request_count = 0
        for tweet in reversed(marks):
            try:
                print ('Deleting like #', request_count, tweet.id, end='')
                api.DestroyFavorite(status_id=tweet.id)
                print('...unliked!')
                time.sleep(0.1)
                request_count += 1
            except twitter.TwitterError as err:
                if 'No status found with that ID.' in err.message[0]['message']:
                    print('...not found')
                else:
                    print("failed with: %s\n" % err.message)
    else:
        print('No need to unfave any tweets')

