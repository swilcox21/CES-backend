"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'p=340[tp4q[gp[e9-3q4ygh3qh5dsrf]]]'  # Change this!
jwt = JWTManager(app)

# Provide a method to create access tokens. The create_access_token()
# function is used to actually generate the token, and you can return
# it to the caller however you choose.
@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    email = request.json.get('email', None)
    password = request.json.get('password', None)
    if not email:
        return jsonify({"msg": "Missing email parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    usercheck = User.query.filter_by(email=email).first()
    if usercheck == None:
        return jsonify({"msg": "Bad Email"}), 401

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token), 200


# Protect a view with jwt_required, which requires a valid access token
# in the request to access.
@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/user', methods=['GET'])
def get_users():
    users = User.query.all()
    users = list(map(lambda x: x.serialize(), users))
    return jsonify(users), 200

@app.route('/user', methods=['POST'])
def post_user():
    body = request.get_json()
    new_user = User.query.filter_by(email=body['email']).first()
    if new_user is not None:
        raise APIException('this user is already registered', status_code = 404)
    new_user = User(first_name = body['firstName'],
                    last_name = body['lastName'],
                    email = body['email'],
                    password = body['password'])
    db.session.add(new_user)
    db.session.commit()
    user = User.query.filter_by(email=body['email']).first()
    print('UNSERIALIZED', user)
    # user = list(map(lambda x: x.serialize(), user))
    print('SERIALIZED', user)
    return jsonify(user.serialize()), 201

@app.route('/todo/<username>/<int:id>', methods=['PUT'])
def put_todo(username, id):
    body = request.get_json()
    todo_item = Todo.query.get(id)
    print("MYTODOITEM", todo_item)
    todo_item.done = body['done']
    todo_item.label = body['label']
    db.session.commit()
    updated_item = Todo.query.get(id)
    updated_item = updated_item.serialize()
    return jsonify(updated_item), 200

@app.route('/user/<email>/<int:id>', methods=['DELETE'])
def delete_user(email, id):
    user = User.query.get(id)
    if user is None:
        raise APIException('user does not exist', status_code = 400)
    db.session.delete(user)
    db.session.commit()
    user = User.query.filter_by(email = email)
    # user = list(map(lambda x: x.serialize(), User))
    return jsonify(user), 202

# @app.route('/cart/<email>', methods=['GET'])
# def get_cart():
#     cart = Cart.query.all()
#     cart = list(map(lambda x: x.serialize(), cart))
#     return jsonify(cart), 200

# @app.route('/cart/<email>', methods=['POST'])
# def post_cart_item(email,id):
#     body = request.get_json()
#     new_cart = Cart.query.filter_by(email=body['email']).first()
#     if new_cart is not None:
#         raise APIException('this item is already in your cart', status_code = 404)
#     new_cart = Cart(email = body['email'],
#                     name = body['name'],
#                     unit_price = body['unitPrice'],
#                     sub_total = body['subTotal'],
#                     color = body['color'],
#                     size = body['size'],
#                     units = body['units'],
#                     image = body['image'])
#     db.session.add(new_cart)
#     db.session.commit()
#     cart = Cart.query.filter_by(email=body['email']).first()
#     print('UNSERIALIZED', cart)
#     print('SERIALIZED', cart)
#     return jsonify(cart.serialize()), 201

# @app.route('/cart/<email>/<int:id>', methods=['DELETE'])
# def delete_cart_item(email, id):
#     cart_item = Cart.query.get(id)
#     if cart_item is None:
#         raise APIException('item does not exist', status_code = 400)
#     db.session.delete(cart_item)
#     db.session.commit()
#     cart = Cart.query.filter_by(email = email)
#     cart = list(map(lambda x: x.serialize(), Cart))
#     return jsonify(Cart), 202

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
