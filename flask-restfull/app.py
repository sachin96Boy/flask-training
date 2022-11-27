from flask import Flask
from flask_restful import  Api 
from dotenv import load_dotenv
from flask_jwt import JWT
import os

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)
app.secret_key = os.getenv("SECREAT_KEY")
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth
# in python 3.10, it gives an import error for jwt_required
# so i downgraded to  ver 3.7 to see if it work


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
# this endpoint will be /student/<string:name> 

app.run(port=5000, debug=True)

