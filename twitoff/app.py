"""
Main app/routing file for twitoff
"""

from os import getenv
from flask import Flask, render_template, request
from .models import DB, User
from .twitter import add_or_update_user, update_all_users
from .prediction import predict_user
from dotenv import load_dotenv

# creates application
def  create_app():
    """
    Create a config of the flask application
    """
    app = Flask(__name__) 

    # database and app configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL') 
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    
    #innistializes Data_base
    DB.init_app(app)

    #decorator able to edit a function without making an overriding change 
    @app.route('/') 
    def root():
        # renders base.html template and passes down title and users
        return render_template('base.html', title='Home', users=User.query.all())

    # @app.route('user', method=['POST'])   #@app.route is a dec
    @app.route('/compare', methods=['POST'])
    def compare():
        user0, user1 = sorted([request.values['user0'],
                                    request.values['user1']])
        if user0 == user1:
            message = 'Cannot compare a user to themselves'
        else:
            prediction = predict_user(user0,
                                            user1,
                                            request.values['tweet_text'])

            message = '{} is more likely to be said by {}'.format(
                            request.values['tweet_text'], 
                            user0 if prediction else user1,
                            user1 if prediction else user0)

        return render_template('prediction.html',
                                        title='Prediction',
                                        message=message)

    @app.route('/user', methods=["POST"])

    @app.route('/user/<name>', methods=['GET'])
    def user(name=None, message=' '):
        name = name or request.values["user_name"]
        try:
            if request.method =='POST':
                add_or_update_user(name)
                message = "user {} successfully added!"

            tweets = User.query.filter(User.name == name).one().tweets

        except Exception as yeet:
            message = f"Error adding {name}:  {yeet}"
            tweets = []
        return render_template('user.html',
                                        title=name,
                                        tweets=tweets,
                                        message=message)

    @app.route('/update')
    def update():
        update_all_users()
        return render_template('base.html',
                                        users=User.query.all(),
                                        title='All tweets updated')

    @app.route('/reset')
    def reset():
        DB.drop_all() #delates data base that is present
        DB.create_all() #create the database from scratch
        return render_template("base.html",
                                        title="Reset database!",
                                        users=User.query.all())

    

    return app