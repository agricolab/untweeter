## How To
- install the module (i personally prefer in editable mode for easier updating)
    ```{bash}
    git clone https://github.com/agricolab/untweeter.git
    cd untweeter
    pip install -e .
    ```
- Run in the terminal and fill in consumer_key, consumer_secret, access_token_key, access_token_secret.  It also sets the maximum of tweets and faves to 100
    ```{bash}
    python -m untweeter --ask-for-keys --tweet-limit 100 --fave-limit 100
    ```
-  To acquire keys,
    - Apply for a Twitter Developer account https://developer.twitter.com/en/apps
    - Create a Twitter app
    - Fill in the details
    - Take note of the keys
- You only need to fill out all of this once, afterwards untweeter read everything from an inifile in your user directory. Please note, that this means your access codes are stored in plain text. Treat with caution!
- If you later want to remove tweets and faves above the limit just run
```{bash}
    python -m untweeter
```
- If you want a dry run without any actual deletion, add ```--dry```


## Limitations

The limits is max 200 each for tweets and faves, as twitter does not return more than if you request the ids of old faves with the API.


### Batch delete old faves
Due to the way twitter handles older faves, they can no longer be unliked by the API without liking them first again. If you want to remove the older ones, you need to request your twitter archive and download it. Inside of this archive, there will be a file called 'like.js', where all your likes are listed.

If you want to delete older faves, please be aware that twitter stores them in a weird fashion. Unfaving them requires faving them again, and then unfaving. Key caveat is that such behavior can appear as if you are stalking or your account has been hijacked. Check this post for a discussion of this approach : https://medium.com/@melissamcewen/how-to-completely-delete-your-twitter-likes-5a41c35aefb8

Anyways, to do this you can follow this examples:
- You obviously need the API keys, so in case you haven't done already, set up a developer account with twitter, get the keys and run
    ```
    python untweeter --ask-for-keys
    ```
- Request your data from twitter (in the settings) https://twitter.com/settings/your_twitter_data
- Download and unzip
- take note of the path to like.js
- run
    ```{bash}
    python -m untweeter.batch --path /path/to/like.js
    ```
- Delete the oldest 100 (up to 1000 in 24 hours due to API rate limits set by twitter) of your old faves
    ``` {bash}
    python -m untweeter.batch --delete 100
    ```
- Again, if you want a dry run without any actual deletion, add ```--dry```
