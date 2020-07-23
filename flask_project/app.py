# Import modules
from flask import Flask, render_template, redirect, url_for, request, abort

username = "admin"
password = "admin"
i = 0

# Create flask instance
app = Flask(__name__)

# Create index method
@app.route('/')
def index():
    return render_template('base.html')

# Create log in method
@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    i = 0
    if request.method == 'POST':
        if request.form['username'] != username or request.form['password'] != password:
            if i >= 3:
                error = 'You have failed too many times.'
                abort(404)
            else:
                error = 'Invalid Credentials. Please try again. {}'.format(i)
        else:
            return "<h3> Access your user page <a href=http://127.0.0.1:5000/login/{} > here </a> </h3>".format(username)

    return render_template('log_in.html', error=error)

@app.route("/login/<username>")
def welcome_user(username):
    return f"<h1>Welcome to Python flask app, {username} </h1>"

# Run app
if __name__ == "__main__":
    app.run()
