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
- To run code use below code
```python
if __name__ == "__main__":
    app.run()
```
- Then type flask run in terminal
