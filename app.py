# May need to do pip install flask first
# Importing flask module
from flask import Flask
from markupsafe import escape

# To use flask need to create instance of the app
app = Flask(__name__)

# Specifies route to access application. Known as a decorator
@app.route("/")
# Create welcome method to display on home/default page
def index():
    # Printing test text
    return ("<h1>Welcome to my MVC Flask project!<h1/>"), ("\n Click here: http://127.0.0.1:5000/welcome")

# One way to get user input on flask website
@app.route('/welcome/')
def welcome_user():
    username = input("Enter a name here")
    return "Welcome, I hope you enjoy the website, {}!".format(username)

# Another way, using flask arguments during run time
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

# Running the app
if __name__ == "__main__":
    # Debug = true updates change without rerunning app
    app.run(debug=True)
