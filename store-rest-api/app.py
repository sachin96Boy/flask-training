from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# lets define a set of dummy stores to return in get request
stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]



@app.route('/store', methods=['POST'])
# POST - used to receive data
#create a store with a given name
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
# The <> brackets tell Flask that the part of the URL that is inside the brackets is a variable, and that we want to pass it as a parameter to our function.
# The <string:name> part tells Flask that the variable will be a string.
def get_store(name):
    pass

@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass


app.run(port=5000)