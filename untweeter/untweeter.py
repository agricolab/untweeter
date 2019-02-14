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
                print ('Untweeting #', request_count, tweet.id, end='')
                api.DestroyStatus(status_id=tweet.id)
                print('...untweeted!')
                time.sleep(0.1)
                request_count += 1
            except twitter.TwitterError as err:
                if err.message[0]['code'] == 142:
                    print('...account is protected')
                elif err.message[0]['code'] == 50:
                    print('...user not found')
                elif err.message[0]['code'] == 144:
                    print('...tweet not found')
                else:
                    print("failed with: %s\n" % err.message)
    else:
        print('No need to untweet any tweets')

def unlike(api, restrict=100, args=None):
    faves = api.GetFavorites(count=200, include_entities=False)
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
                print ('Unfaving #', request_count, tweet.id, end='')
                api.DestroyFavorite(status_id=tweet.id)
                print('...unfaved!')
                time.sleep(0.1)
                request_count += 1
            except twitter.TwitterError as err:
                if err.message[0]['code'] == 142:
                    print('...account is protected')
                elif err.message[0]['code'] == 50:
                    print('...user not found')
                    api.DestroyFavorite(status_id=tweet_id)
                    print('...unfaved!')
                elif err.message[0]['code'] == 144:
                    print('...tweet not found')
                else:
                    print("failed with: %s\n" % err.message)
    else:
        print('No need to unfave any tweets')

