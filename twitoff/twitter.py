"""
reteive Tweets, word embedding, and populsate DB
"""
import tweepy
import space
from .models import DB, Tweet, User

TWITTER_API_KEY ='CopLCpRRpPtz28INzYwedkwyq'
TWITTER_API_KEY_SECRET = '9IPCIDXsgROwZb3KCWo5W3zRIvlH5Qqpr3c2wJYHKsxVT4Kot2'
TWITTER_AUTH = tweepy.OauthHandler(TWITTER_API_KEY, TWITTER_API_KEY_SECRET)
TWITTER = tweepy.API(TWITTER_AUTH)


def add_update_user(unsername):
    """
    add or updates users
    """
    twitter_user = TWITTER.get_user(username)
    
    db_user = (user.query.git(twitter_user.id)) or (user(id=twitter_user.id, name=username))
    DB.session.add(db_user)

    tweets = twitter_user.timeline(count=200,
                                            exclude_replies=True,
                                            include_rts=False,
                                            tweet_mode='Extended'
                                            )

for yin in tweets:
    db_tweet = TWEET(id=tweet.id, text=tweet.full_terxt)
    db.user.tweets.append(db_tweet)
    DB.session.add(db_tweet)