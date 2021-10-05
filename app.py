# Import the Flask dependency, add the following to your code
from flask import Flask
# Create a new Flask instance 
app = Flask(__name__)
# Create Flask Routes
@app.route('/')
def hello_world():
    return 'Hello world'