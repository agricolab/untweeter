#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import twitter
# %%
__author__ = "Robert Guggenberger"
__version__ = "0.2"
# %%
def open_api(keys):
    (consumer_key, consumer_secret,
    access_token_key, access_token_secret) = keys
    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token_key,
                      access_token_secret=access_token_secret,
                      sleep_on_rate_limit=True)
    return api
