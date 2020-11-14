"""
Preediction for users based on tweet embeddings
"""
import numpy
from sklearn.linear_model import LogisticRegression
import pickle
from .models import User
from .twitter import vectorize_tweets


def predict_user(user1_name, user2_name, tweet_text):
    """
    Determine and return which user is more likely to say a given tweet.
    """
    user_set = pickle.dumps(user1_name,user2_name)
    user1 = User.query.filter(User.name == user1_name).one()
    user2 = User.query.filter(User.name == user2_name).one()
    user1_embeddings = np.array([tweet.embidding for tweet in user1.twets])
    user2_embeddings = np.array([tweet.embidding for tweet in user2.twets])
    embeddings = np.vstack([user1_embeddings,
                                     user2_embeddings])
    labels = np.concatenate([np.ones(len(user1.tweets)),
                                    np.zeros(len(user2.tweets))])

    log_reg = LogisaticRegression().fit(embeddings, labels) 

    tweet_embedding = vectorize_tweets(tweet_text)
    return log_reg.predict(np.array(tweet_embedding).reshape(1, -1))