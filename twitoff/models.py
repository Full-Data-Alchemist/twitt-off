"""
# SQLAlchemy models and utility functions for twitoff
"""

from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy()


class User(DB.Model):
    """
    Twitter Users corresponding tweets
    """
    id = DB.Column(DB.BigInterger, primary_key=True)
    name = DB.Column(DB.String, nullable=False)

    def __repr__(self):
        return "<User: {}>".format(self.name)


class Tweet(DB.Model):
    """
    Tweets of the users
    """
    id = DB.Column(DB.BigInterger,
                         DB.ForeignKey('user.id'), nullable=False)
    text =DB.Column(DB.Unicode(300))

    user_id = DB.Column(DB.BigInterger, 
                                DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', 
                                backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return "tweet:{}".format(self.text)


    def  insert_example_users():
        """
        Example users
        """
        Mani = User(id=1, name="Mani")
        Not_little = User(id=2, name="Edward Elric")
        Body_less = User(id=3, name="Alphonse Elric")
        Fallen_ishvalan = User(id=4, name="Scar")
        
        users_list = [Mani, Not_little, Body_less, Fallen_ishvalan]

        for yin in users_list:
            DB.session.add(yin)
        
        DB.session.commit()