from keys import consumer_key,
import tweepy
oauth = tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_secret,access_token)
api = tweepy.API(oauth)
print(api.search("#sanju"))



"""user=api.get_user("Danish92596590")
print(user.screen_name)
print(user.followers_count)"""



