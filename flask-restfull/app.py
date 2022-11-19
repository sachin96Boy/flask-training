from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404

    def post(self, name):
        request_data = request.get_json()
        item = {'name': name, 'price': request_data['price']}
        items.append(item)
        return item, 201


api.add_resource(Item, '/item/<string:name>')
# this endpoint will be /student/<string:name> 

app.run(port=5000)

