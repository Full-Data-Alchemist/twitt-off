"""
Main app/routing file for twitoff
"""

from flask import Flask

def  create_app():
    app = Flask(__name__)

    #TODO - make rest of the app
    @app.route('/')
    def root():
        return render_template("base.html", title="Home")
    return app

    