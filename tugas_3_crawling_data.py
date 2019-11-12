# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:18:31 2019

@author: asus
"""

import tweepy
import pandas
from tweepy import OAuthHandler, Stream, StreamListener
import csv

n=int(input("masukkan jumlah topik = "))
topik=[]
for i in range (n):
    temp=str(input("masukkan topik ke-{} = ".format(i+1)))
    topik.append(temp)


consumer_key="QYvHeIdpM7MuxDNYpvDmTO6gf"
consumer_secret="kk81ZHN31ZMCGeioVieXH9xevucVVrAYwSSEiPQhTQrUXfd3K2"
access_token="289218050-v6AisxlJUmVkv3jLcJo1599ZVxp3rsoJjUyz6NPW"
access_token_secret="FN8r1nz2SVbloma4mobVGut5VF4Ch4lT2DWGKL8rL4bZf"
auth=OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

#csvFile = open('nama.csv', 'a')
#csvWriter = csv.writer(csvFile)

list0=[]
list1=[]
for i in range (n):
    for tweet in tweepy.Cursor(api.search,q=topik[i],count=5,
                           lang="id").items():
        list0.append(tweet._json)
        data=pandas.DataFrame(list0)
        data1=data[['text','created_at']].head()
    list1.append(data1)


export_csv = list1.to_csv (r'D:\FGA\digitalent2\export_dataframe3.csv', header=True)
print("")
print("EXPORT TO CSV SUCCESS!!!")
print(data1)