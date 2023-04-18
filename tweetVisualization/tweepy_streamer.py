import tweepy
import tweet_file

auth = tweepy.OAuthHandler(
    tweet_file.consumer_key, tweet_file.consumer_secret
    )

auth.set_access_token(tweet_file.access_token, 
    tweet_file.access_token_secret
    )

api = tweepy.API(auth)

public_tweets = api.available_trends()

#for tweet in public_tweets:
#    print (tweet.text)
