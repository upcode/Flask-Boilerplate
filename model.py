##############################################################################
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



# This is the connection to the SQLite database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)
db = SQLAlchemy()

#-MODEL TABLES FOR DB------------------------------------------------------------------------#
#example of user model
class User(db.Model):
    __tablename__ = 'users'


    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    username = db.Column(db.String(20), nullable=True)



















#-HELPER FUNCTIONS-----------------------------------------------------------------------------#

def connect_to_db(app):
    """Connect the database to our Flask App"""
    # Configure to use our POSTGRES database
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgressql:///localhost/wdatabasedb'
   
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.app = app
    db.init_app(app)

##############################################################################


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from routes import app
    connect_to_db(app)
    print "Connected to DB."