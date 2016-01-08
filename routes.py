from flask import Flask
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_wtf import Form
from jinja2 import StrictUndefined
from flask_debugtoolbar import DebugToolbarExtension

#unhash to connect to db
# from model import connect_to_db, db

#-FLASK CONFIGS---------------------------------------------------------------------------#

app = Flask(__name__)

app.secret_key = 'LEGENDARY'
app.jinja_env.undefined = StrictUndefined

#-ROUTES---------------------------------------------------------------------------#
                        
@app.route("/")
def hello():
    return "Hello World!"
    # unhash this when I want to test 
    # return render_template("test.html")



@app.route("/index")
def index():
   return render_template("index.html")




#-HELPER FUNCTIONS--------------------------------------------------------------------#



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    app.debug = True
    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.run()