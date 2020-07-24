# Import modules, as well as previous code
from flask import Flask, render_template, request, abort, session
from csv_interaction import *

# Creating and reading from the CSV file, specifying username to be created
write_csv("Jeff", "password")
user_details = read_csv()

# Creating username and password variables by fetching values from CSV dictionary
username = user_details["username"]
password = user_details["password"]

# Create flask instance
app = Flask(__name__)
# Creating secret key to session variables function
app.config['SECRET_KEY'] = "timberlake1990"

# Create index method
@app.route('/',methods=['GET'])
def index():
    # Creating session variable
    session["attempt"] = 3
    # Using html template
    return render_template('base.html')


# Create log in method
@app.route('/login/', methods=['GET', 'POST'])
def login():
    # Creating empty error variable for later
    error = None
    # Running code only if method is post(sending data to server)
    if request.method == 'POST':
        # Checking username and password inputted are same as variables
        encrypted_input = encrypt_input(request.form['password'])
        if request.form['username'] != username or encrypted_input != password:
            # Getting session attribute using pop method
            attempt_num = session.pop("attempt", None)
            # Using attempt number in if loop to limit attempts to 3 times
            if int(attempt_num) == 0:
                # Aborting website to 404 errors if too many attempts
                abort(404)
            else:
                # Counting down password attempts
                attempt_num -= 1
                # Recreating attempt counter
                session["attempt"] = attempt_num
                # Error message to be displayed
                error = 'Invalid Credentials. Please try again.'
        else:
            # Giving link to user page if username/password correct
            return "<h3> Access your user page <a href=http://127.0.0.1:5000/login/{} > here </a> </h3>".format(username)
    # Using log in template
    return render_template('log_in.html', error=error)

# Specifying message displayed after succesful log in
@app.route("/login/<username>")
def welcome_user(username):
    # Defining specifics and style of message
    text_output = "<body style='background-color:mistyrose;'>" \
                  "<span style='font-size:100px;'>&#128578;</span>" \
                  "\n<h1>Welcome to your login  page, {}." \
                  " Did you know Birds have hollow bones? </h1>".format(username)
    return text_output

# Run app
if __name__ == "__main__":
    app.run()
