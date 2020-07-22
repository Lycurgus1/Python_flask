# Import modules
from flask import Flask, render_template, redirect, url_for, request

# Create flask instance
app = Flask(__name__)

# Create log in method
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return "Success!"
    return render_template('base.html', error=error)

# Run app
if __name__ == "__main__":
    app.run()
