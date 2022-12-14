from  flask_restful  import  Resource ,  reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from modals.item import ItemModel


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field cannot be left blank!")
    parser.add_argument('store_id', type=int, required=True, help="Every item needs a store id.")

    @jwt_required()
    def get(self, name):
        try:
            item = ItemModel.find_by_name(name)
        except:
            return {"message": "An error occurred finding the item."}, 500
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
        request_data = Item.parser.parse_args()
        item = ItemModel(name, **request_data)
        
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500
        
        return item.json(), 201

    @jwt_required()
    def delete(self, name):
       claims = get_jwt_identity()
       if not claims['is_admin']:
             return {'message': 'Admin privilege required.'}, 401 
       item = ItemModel.find_by_name(name)
       if item:
          item.delete_from_db()
       return {'message': 'Item deleted'}

    def put(self, name):
        
        request_data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **request_data)
        else:
            item.price = request_data['price']

        item.save_to_db()
        return item.json()


class ItemList(Resource):

    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
