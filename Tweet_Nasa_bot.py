# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 15:17:40 2023

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




base_path = 'X:/XPLOR/BuildHeightMap/WebScrappers'
file = 'Mars_Nasa.pkl'
file_path = os.path.join(base_path,file)
df = pd.read_pickle(file_path)

df=df.sort_values(by='Date',ascending=True).reset_index(drop=True)

n_elements=len(df)

for index,row in df.iterrows():
    if not row.Twitted:
        tweet = row.Title + "\n" + row.Paragraph + "\n" + row.Link
        try : 
            a=api.update_status(status=tweet)
            df.at[index,'Twitted']='True'
            break
        except tweepy.errors.TweepyException as e:
            print(e)

df.to_pickle(file_path)

            
        
        






# Post a tweet with an image
# tweet = 'Where is Curiosity today? (https://mars.nasa.gov/msl/mission/where-is-the-rover/) Soon I will present a #Mars #DigitalTwin where you will be able to see what Curiosity is doing. (www.xplorcode.com)'
# image_path = 'X:/XPLOR/BuildHeightMap/WhereIsCuriosity.png'
# media = api.media_upload(image_path)
# api.update_status(status=tweet, media_ids=[media.media_id])


