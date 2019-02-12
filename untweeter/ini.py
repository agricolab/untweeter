import configparser
import os
# %%
class Ini():

    def __init__(self, path=None):
        self.ini = configparser.ConfigParser()
        if path is None:
            path = os.path.split(__file__)[0]
            path = path.split('/untweeter')[0]
            self.path = os.path.join(path, 'untweeter/untweeter.ini')
            self.ini.read(self.path)

    def write(self):
        with open(self.path, 'w') as f:
            self.ini.write(f)
        self.ini.read(self.path)

    def set_tweet_limit(self, limit:int):
        self.ini.set('LIMITS', 'tweets', value=str(limit))
        self.write()

    def set_fave_limit(self, limit:int):
        self.ini.set('LIMITS', 'faves', value=str(limit))
        self.write()

    def get_limits(self):
        restrict_tweets = self.ini.getint('LIMITS', 'tweets')
        restrict_faves = self.ini.getint('LIMITS', 'faves')
        restrict_tweets = max(0, min(200, restrict_tweets))
        restrict_faves = max(0, min(200, restrict_faves))
        return restrict_tweets, restrict_faves

    def get_keys(self):
        consumer_key =  self.ini.get('KEYS','consumer_key')
        consumer_secret = self.ini.get('KEYS','consumer_secret')
        access_token_key = self.ini.get('KEYS','access_token_key')
        access_token_secret = self.ini.get('KEYS','access_token_secret')
        return (consumer_key, consumer_secret,
                access_token_key, access_token_secret)

    def ask_for_keys(self):
        consumer_key =  input('consumer_key: ')
        consumer_secret = input('consumer_secret: ')
        access_token_key = input('access_token_key: ')
        access_token_secret = input('access_token_secret: ')
        self.ini.set('KEYS','consumer_key', consumer_key)
        self.ini.set('KEYS','consumer_secret', consumer_secret)
        self.ini.set('KEYS','access_token_key', access_token_key)
        self.ini.set('KEYS','access_token_secret', access_token_secret)
        self.write()

    def set_old_faves(self, fave_ids):
        self.ini.remove_section('LIKEJS')
        self.ini.add_section('LIKEJS')        
        for fid in fave_ids:
            self.ini.set('LIKEJS',str(fid),'FALSE')
        self.write()
                    
    def get_old_faves(self, count=500):        
        fave_ids = self.ini.options('LIKEJS')        
        if (not fave_ids) or (count==0):
            return None
        else:
            return [int(fid) for fid in fave_ids[-count:]]
    
    def remove_old_fave(self, fave_id):
        self.ini.remove_option('LIKEJS', str(fave_id))
        self.write()
        