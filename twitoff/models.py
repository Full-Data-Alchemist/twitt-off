#TWITTOFF/twitoff/Models.py
"""
SQLAlchemy models and utility functions for twitoff
"""

from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy()


class User(DB.Model): #creates a usesr table
    """
    Twitter Users corresponding tweets
    """
    id = DB.Column(DB.BigInteger, 
                        primary_key=True) #id column Primary key
    name = DB.Column(DB.String,    #new column
                            nullable=False) #name column   
    newest_tweet_is = DB.Column(DB.BigInteger) # newest tweet column
    
    
    def __repr__(self):
        return f"<User:{self.name}>"


class Tweet(DB.Model):
    """
    Tweets of the users
    """
    id = DB.Column(DB.BigInteger,
                         primary_key=True)
    text =DB.Column(DB.Unicode(300))
    vect = DB.Column(DB.PickleType,
                            nullable=False)
    user_id = DB.Column(DB.BigInteger, 
                                DB.ForeignKey('user.id'),
                                nullable=False)
    user = DB.relationship('User', 
                                backref=DB.backref('tweets',
                                lazy=True))

    def __repr__(self):
        return f"tweet:{self.text}"

    # interernal testing feature
    def  insert_example_users():
        """
        Example users
        """
        Mani = User(id=1, name="Mani")
        Not_little = User(id=2, name="Edward Elric")
        Body_less = User(id=3, name="Alphonse Elric")
        Fallen_ishvalan = User(id=4, name="Scar")
        
        users_list = [Mani, Not_little, Body_less,
                        Fallen_ishvalan]

        for yin in users_list:
            DB.session.add(yin)
        
        DB.session.commit()



#random strech goal for self
# import random

#     def random_tweet(User):
#         User = User.id

#         tweet = []
#         tweets = tweets.append(random.choice())

#         return Tweet()
