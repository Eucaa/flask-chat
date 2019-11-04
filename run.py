import os
from datetime import datetime  #This will import a timestamp
from flask import Flask, redirect, render_template, request, session, url_for

"""
Create a (temp) session-cookie, which will store our username so that when we visit the website, 
it will redirect us to our personal homepage. Add 'request' and 'session' to the `import`-part above.
The session-cookie will cease to exist once the browser has been totally closed off.
"""
app = Flask(__name__)
app.secret_key = "randonstring123" #Generally in production, this will be set as an environment variable like an IP address import.
messages = []

def add_message(username, message):
    """Add messages to the `messages` list"""
    now = datetime.now().strftime("%H:%M:%S") #The strftime() method takes a date/time object and converts it into a string according to a given format.
    
    """Create dictionary to store message information(data) as key-value pairs."""
    messages.append({"timestamp": now, "from": username, "message": message}) #append the whole messages dictionary.

    """ timestamp will store the value of `now` (%H:%M:%S)
        from will store the value username, and thus the username of the user
        message will store the value message, which will be the written text on screen
    """
    


@app.route('/', methods = ["GET","POST"]) #Create these methods to make "GET" and "POST" active, in correspondance with index.html.
def index():

    """Main page with instructions"""
    if request.method == "POST": #If request.method is equal to "POST" then create a new var in session called ["username"].
        session["username"] = request.form["username"] #The ["username"] of session must be equal to that of the request.form.

    if "username" in session: #If the username here and in session are the same, then redirect to the session username, taking us to this route.
        return redirect (url_for("user", username=session["username"])) 

    return render_template("index.html")


@app.route("/chat/<username>", methods= ["GET", "POST"]) 
#The 'user view'. Written this way, it will get treated as a variable. "GET" and "POST" correspond with chat.html.

def user(username): #This function is going to bind to the root decorator above ( @app.route ).

    """Add and display chat message"""
    if request.method == "POST": #If request.method is equal to "POST" then get these varaibles:
        username = session["username"] #Get the username from the session.
        message = request.form["message"] #Get the message from the form.
        add_message(username, message)  #Then call for the add_messages function and it's functionality. 
        return redirect(url_for("user", username=session["username"]))

    return render_template("chat.html", username= username, chat_messages= messages) 

#app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)

if __name__ == '__main__':
    port_number = os.environ.get('PORT')
    if isinstance(port_number, str):
        port_number = int(port_number)
    if not port_number:
        port_number = 5000
    app.run(debug=False, host="0.0.0.0", port=port_number)

