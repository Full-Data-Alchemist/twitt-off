"""
# SQLAlchemy models and utility functions for twitoff
"""


from flask_sqlalchemy import SQLAlchemy



DB = SQLAlchemy()


class User(DB.Model):
    """
    Twitter Users
    """
    id = DB.Column(DB.BigInterger, primary_key=True)
    name = DB.COlumn(DB.String, nullable=False)

    def __repr__(self):
        return "<User: {}>".format(self.name)