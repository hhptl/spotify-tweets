import sys

import tweepy
from unshortenit import UnshortenIt

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

#method to get a user's last tweets
def get_tweets(username):

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#set count to however many tweets you want
	number_of_tweets = 500

	#get tweets
	for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items(number_of_tweets):
        #create array of tweet information: username, tweet id, date/time, text
		if("https://t.co/" in tweet.text):
			index = (tweet.text).index('https://t.co')
			t_url = (tweet.text)[index:(index+24)]
			unshortener = UnshortenIt()
			url = unshortener.unshorten(t_url)
			if("open.spotify" in url):
				print(url)
			#print(url)
		#print (tweet.text)

#if we're running this as a script
if __name__ == '__main__':

    #get tweets for username passed at command line
    if len(sys.argv) == 2:
        get_tweets(sys.argv[1])
    else:
        print ("Error: enter one username")
