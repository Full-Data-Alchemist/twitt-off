"""
Preediction for users based on tweet embeddings
"""
import numpy as np
from sklearn.linear_model import LogisticRegression
from .models import User
from .twitter import vectorize_tweets
import pickle


def predict_user(user0_name, user1_name, hypo_tweet_text):
    """
    Determine and return which user is more likely to say a given tweet.

    example run: predict_user('elonmusk', 'nasa', 'Tesla cars are in space')
        returns either 0 (user0_name) or 1 (user1_name)
    """
    # user0_vects = np.array([tweet.vect for tweet in user0.tweets])
    # user1_vects = np.array([tweet.vect for tweet in user1.tweets])
    # vects = np.vstack([user0_vects, 
    #                         user1_vects])
    # labels = np.concatenate([np.zeros(len(user0.tweets)),
    #                                 np.ones(len(user1.tweets))])
    # hypo_tweet_vect = vectorize_tweets(hypo_tweet_text)
    # log_reg = LogisaticRegression().fit(vects, labels)
    # return log_reg.predict(hypo_tweet_vect.reshape(1, -1))
    user_set = pickle.dumps(user0_name,user1_name)
    user0 = User.query.filter(User.name == user0_name).one()
    user1 = User.query.filter(User.name == user1_name).one()
    user0_embeddings = np.array([tweet.embidding for tweet in user0.tweets])
    user1_embeddings = np.array([tweet.embidding for tweet in user1.tweets])
    embeddings = np.vstack([user0_embeddings,
                                     user1_embeddings])
    labels = np.concatenate([np.ones(len(user0.tweets)),
                                    np.zeros(len(user1.tweets))])

    log_reg = LogisaticRegression().fit(embeddings, labels) 

    tweet_embedding = vectorize_tweets(tweet_text)
    return log_reg.predict(np.array(tweet_embedding).reshape(1, -1))