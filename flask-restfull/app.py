from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api
from dotenv import load_dotenv
from flask_jwt import JWT, jwt_required
import os

from security import authenticate, identity

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)
app.secret_key = os.getenv("SECREAT_KEY")
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth
# in python 3.10, it gives an import error for jwt_required
# so i downgraded to  ver 3.7 to see if it work

items = []

class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
        request_data = request.get_json()
        item = {'name': name, 'price': request_data['price']}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
# this endpoint will be /student/<string:name> 

app.run(port=5000, debug=True)

