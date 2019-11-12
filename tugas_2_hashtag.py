# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:11:05 2019

@author: asus
"""

import tweepy
import csv
from tweepy import OAuthHandler, Stream, StreamListener
 

consumer_key="QYvHeIdpM7MuxDNYpvDmTO6gf"
consumer_secret="kk81ZHN31ZMCGeioVieXH9xevucVVrAYwSSEiPQhTQrUXfd3K2"
access_token="289218050-v6AisxlJUmVkv3jLcJo1599ZVxp3rsoJjUyz6NPW"
access_token_secret="FN8r1nz2SVbloma4mobVGut5VF4Ch4lT2DWGKL8rL4bZf"
auth = OAuthHandler(consumer_key, consumer_secret,)
auth.set_access_token(access_token, access_token_secret)
api =  tweepy.API(auth)


csvFile = open('tugas2.csv', 'a')
csvWriter = csv.writer(csvFile)
for tweet in  tweepy.Cursor(api.search,q="#StandUpforX1", lang="en",count=200, since="2019-10-10").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')]) #"#StandUpforX1" isi hashtag yang ingin dicari