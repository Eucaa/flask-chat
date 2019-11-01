import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "To send a message use /USERNAME/MESSAGE"
"""Main page with instructions"""

@app.route("/<username>") #This way, it will get treated as a variable.
def user(username): #This function is going to bind to our root decorator.
    return "Hi" + username

@app.route("/<username>" + "/<message>")
def send_message(username, message):
    return "{0}: {1}".format(username, message)  

#app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)

