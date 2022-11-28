from flask import Flask
from flask_restful import  Api 
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
import os


from resources.user import UserRegister, User, UserLogin
from resources.item import Item, ItemList
from resources.store import Store, StoreList

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///test.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JWT_SECRET_KEY'] = os.getenv("SECREAT_KEY")
api = Api(app)

# this is a special decorarter that will create the tables in the database
#it'll run before the first request
@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWTManager(app)  # /auth endpoint is only used in flask-jwt not in flask-jwt-extended
# in python 3.10, it gives an import error for jwt_required
# so i downgraded to  ver 3.7 to see if it work

@jwt.user_identity_loader
def add_claims_to_jwt(identity):
    if identity == 1:
        return {'is_admin': True}
    return {'is_admin': False}    



api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')
# this endpoint will be /student/<string:name> 

# we are importing db hre
# because of circular imports 

from db import db
db.init_app(app)

app.run(port=5000, debug=True)

