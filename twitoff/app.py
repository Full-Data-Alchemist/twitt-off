"""
Main app/routing file for twitoff
"""

from flask import Flask, render_template
from .models import DB, User

def  create_app():
    """
    Create a config of the flask application
    """

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3" #where DB is stores 
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    DB.init__app(app)
    #TODO - make rest of the app
    @app.route('/')
    def root():
        DB.drop_all() #delates data base that is present
        DB.create_all() #create the database from scratch
        insert_example_users()
        return render_template("base.html", title="Home", users=User.query.all())



    #new run new application
    #
    return app

    