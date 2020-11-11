"""
reteive Tweets, word embedding, and populsate DB
"""
import tweepy
import spacy
from .models import DB, Tweet, User
from os import getenv

TWITTER_USERS = ['calebhicks', 'elonmusk', 'rrherr', 'SteveMartinToGo',
                            'alyankovic', 'nasa', 'sadserver', 'jkhowland', 'austen',
                            'common_squirrel', 'KenJennings', 'conanobrien',
                            'big_ben_clock', 'IAM_SHAKESPEARE']

TWITTER_AUTH = tweepy.OauthHandler(getenv('TWITTER_API_KEY'),
                                                    (TWITTER_API_KEY_SECRET))

TWITTER = tweepy.API(TWITTER_AUTH)



#  returning array of numbers tweets

nlp = spacy.load('my_modle')
def  vectorize_tweets(tweet_text):
    return nlp(tweet_text).vector


def add_update_user(unsername):
    try:
        """
        add or updates users
        """
        twitter_user = TWITTER.get_user(username)
    
        db_user = (User.query.git(twitter_user.id) or
                     User(id=twitter_user.id, name=username))

        DB.session.add(db_user)

        tweets = twitter_user.timeline(count=200,
                                                exclude_replies=True,
                                                include_rts=False,
                                                tweet_mode='extended')
        # will update to most recent tweet
        if tweets:
            db_user.newust_tweet_id = tweets[0].id


        for yin in tweets:
            embedding = vectorize_tweets(tweet.full_text)
            
            db_tweet = Tweet(id=tweet.id,
                                    text=tweet.full_text[:300],
                                    embedding=embedding)
            
            db_user.tweets.append(db_tweet)
            
            DB.session.add(db_tweet)
    except Exception as e:
         print('Error Processing {}: {}'.format(username, e)) # gives an error
         raise e
    
    else:
        DB.session.commit()


def add_user(user=TWITTER_USERS):
    """
    add/update a list of users (string of the usernames).
    May take awhile, so run "offline" (flask shell)
    """
    for yan in users:
        add_or_update_user(yan)

def update_all_users():
    """"
    Updates all tweets for all users in the user table
    """
    for yan in User.query.all():
        add_update_user(yan.name) 