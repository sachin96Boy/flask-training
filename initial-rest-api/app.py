from flask import Flask

app = Flask(__name__)
# __name__ is a special variable in Python that is set to the name of the module in which it is used.

@app.route('/')
# The route() function of the Flask class is a decorator, which tells the application which URL should call the associated function.
# In this case, we want the home page of our site to be accessible at the URL /, so we've mapped that to our home() function.
def home():
    return "Hello, World!"

app.run(port=5000)
# The run() method of Flask class runs the application on the local development server.
# The app.run() method takes optional host and port parameters to specify the hostname and the port of the server.
# The default port is 5000, which we have used in our example.

# Run the app.py file in the terminal using the command: python app.py
