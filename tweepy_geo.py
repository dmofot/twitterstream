#-------------------------------------------------------------------
# Name:       tweepy_geo.py
# Purpose:    Pull a filtered version of the Twitter public stream.
# Author:     DT
# Created:    01/12/2015
# Python Version:   2.7.8
#-------------------------------------------------------------------

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

consumer_key = "API_KEY_HERE"
consumer_secret = "API_SECRET_HERE"
access_token = "ACCESS_TOKEN_HERE"
access_token_secret = "ACCESS_TOKEN_SECRET_HERE"

class listener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=['#esri', '#arcgis', '#qgis'])