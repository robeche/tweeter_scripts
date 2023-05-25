# -*- coding: utf-8 -*-
"""
Created on Thu May 25 07:52:36 2023

@author: rober
"""

import tweepy
import os

from datetime import datetime, timedelta

import pandas as pd

# Fill in your API keys and access tokens
CLIENT_ID = 'SGt5SnBheWFGUXFOZ3VzRTFHQjU6MTpjaQ'
CLIENT_SECRET = '4Co54fxYgWWah_c8cNp5OAVUa6i8SasoJSSSbSEP0O-pYaUS2s'

consumer_key = 'l1yX2jvDwgo9JViKoVKcGgdND'
consumer_secret = 'xHy8vxaidmdvO1eAnNpi4dM6GXvxphjdqT5hyrWg70yVUhVz4I'

bearer_token = 'AAAAAAAAAAAAAAAAAAAAAFR%2FnAEAAAAAiJVYZe3xGE1jeU8eqPOYvyn3UZ4%3Dx6AmZZTgIB9c1uvB3peQDWl0T027RL31CR1tyZ2IigcvgwID1n'
access_token = '1640981277120626689-7kHwbk0FN6e4F3qb05cmm8Nwx9kII6'
access_token_secret = 'Y7MtsToDk6YN49irGuuxvCc3n9RbJiMoTNaDHqzJfa0KL'


# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create a Twitter API object
api = tweepy.API(auth)

# Retrieve the users you're following
for friend in tweepy.Cursor(api.friends, screen_name).items(30):
    print(friend.screen_name)
    
    
    

following_ids = api.get_friend_ids()
followers_ids = api.get_follower_ids()

not_followers = [x for x in following_ids if x not in followers_ids]

uu1 = api.get_user(user_id=u)

for u in not_followers:
    user = api.get_user(user_id=u)
    user.unfollow()
    