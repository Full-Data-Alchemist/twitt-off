"""
reteive Tweets, word embedding, and populsate DB
"""
from os import getenv
import tweepy
import spacy
from .models import DB, Tweet, User

TWITTER_API_KEY = getenv("")
TWITTER_API_KEY_SECRET = getenv("")
TWITTER_AUTH = tweepy.OAuthHandler(getenv('TWITTER_API_KEY'),
                                                    (TWITTER_API_KEY_SECRET))

TWITTER = tweepy.API(TWITTER_AUTH)



#  returning array of numbers tweets
nlp = spacy.load('my_model')

def  vectorize_tweets(tweet_text):
    """
    Veterizes tweets to use a nlp model on it
    """
    return nlp(tweet_text).vector


def add_or_update_user(username):
    try:
        """
        add or updates users
        """
        #grabs users from twitter DB
        twitter_user = TWITTER.get_user(username)
        #adds or updates user
        db_user = (User.query.get(twitter_user.id)
                    or User(id=twitter_user.id, name=username))
        DB.session.add(db_user)

        #grabd tweets FROM twiter_user
        tweets = twitter_user.timeline(count=200,
                                                exclude_replies=True,
                                                include_rts=False,
                                                tweet_mode='extended')
        
        # will update to most recent tweet
        if tweets:
            db_user.newest_tweet_id = tweets[0].id

        for yin in tweets:
            #stores numerical representations
            vectorized_tweets = vectorize_tweets(yin.full_text)
            embedding = vectorize_tweets(yin.full_text)
            
            db_tweet = Tweet(id=yin.id,
                                    text=yin.full_text[:300],
                                    embedding=embedding)
            
            db_user.tweets.append(db_tweet)
            DB.session.add(db_tweet)
   
    except Exception as e:
        print(f'Error Processing {username}: {e}') # gives an error
        raise e
    
    else:
        DB.session.commit()

def update_all_users():
    """"
    Updates all tweets for all users in the user table
    """
    for yan in User.query.all():
        add_or_update_user(yan.name) 