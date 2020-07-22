# Import modules
from flask import Flask, render_template, redirect, url_for, request

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
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return "Success!"
    return render_template('log_in.html', error=error)

# Run app
if __name__ == "__main__":
    app.run()
