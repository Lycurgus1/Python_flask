# Theory
- Index method is called at endpoint
- Displays the home page

- To use flask need to create instance of the app
```python
app = Flask(__name__)
```
- Index function
```python
# Specifies route to access application,
@app.route("/")
# Create welcome method to display on home/default page
def index():
    # Printing test text
    return "Welcome to a MVC Flask project!"
```
**To run code see below**
- If loop and run command. This tells functions to run
```python
if __name__ == "__main__":
    app.run()
```
- Then type flask run in terminal

**Creating more advanced methods**
- User input can be got in the browser as below
```python
# Using flask arguments during run time
@app.route('/user/<username>')
# Specifying arguments to mentioned in run time
def show_user_profile(username):
    # show the user profile for that user, as per username inserted in browser
    return 'User %s' % escape(username)
```

**Benefits of MVC(Model, veiw, controller**
- Enables interaction with users via the web

**Using HTML templates**

**Inheriting blocks in html**
- First mark block for inheritance in parent html file
```html
<head>
        <meta charset="UTF-8">
<!--   # Creating a title block that will be inherited-->
    <title>[% block title %}Engineering 67 {% endblock %} </title>
</head>
```
- Then inherit this in child html class
```html
{% extends "base.html" %}
{% block title %} Home Page {% endblock %}
```