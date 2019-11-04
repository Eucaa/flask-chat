import os
from datetime import datetime  #This will import a timestamp
from flask import Flask, redirect, render_template, request, session

"""
Create a (temp) session-cookie, which will store our username so that when we visit the website, 
it will redirect us to our personal homepage. Add 'request' and 'session' to the `import`-part above.
The session-cookie will cease to exist once the browser has been totally closed off.
"""
app = Flask(__name__)
app.secret_key = "randonstrgin123" #Generally in production, this will be set as an environment variable like an IP address import.
messages = []

def add_messages(username, message):
    """Add messages to the `messages` list"""
    now = datetime.now().strftime("%H:%M:%S") #The strftime() method takes a date/time object and converts it into a string according to a given format.
    
    """Create dictionary to store message information(data) as key-value pairs."""
    messages_dict = {"timestamp": now, "from": username, "message": message}
    """ timestamp will store the value of `now` (%H:%M:%S)
        from will store the value username, and thus the username of the user
        message will store the value message, which will be the written text on screen
    """
    messages.append(messages_dict) #append the whole messages dictionary.


@app.route('/', methods = ["GET","POST"]) #Create these methods to make "GET" and "POST" active, in correspondance with index.html
def index():

    if request.method == "POST": #If request.method is equal to "POST" then create a new var in session called ["username"].
        session["username"] = request.form["username"] #The ["username"] of session must be equal to that of the request.form.

    if "username" in session: #If the username here and in session are the same, then redirect to the session username, taking us to this route.
        return redirect (session["username"]) 

    return render_template("index.html")
"""Main page with instructions"""

@app.route("/<username>") #This way, it will get treated as a variable.
def user(username): #This function is going to bind to our root decorator.
    """Display chat message"""
    return render_template("chat.html", username= username, chat_messages= messages)

@app.route("/<username>" + "/<message>")
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)  

#app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)

