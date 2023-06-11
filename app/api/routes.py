from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Whiskey, whiskey_schema, whiskeys_schema
import secrets

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getData():
    return {'yee': 'haw'}

@api.route('/whiskey', methods = ['POST'])
@token_required
def whiskeydeets(current_user_token):
    whiskey_name = request.json['whiskey_name']
    whiskey_brand = request.json['whiskey_brand']
    whiskey_location = request.json['whiskey_location']
    whiskey_price = request.json['whiskey_price']
    whiskey_token = current_user_token.token

    whiskey = Whiskey(whiskey_name, whiskey_brand, whiskey_location, whiskey_price, whiskey_token = whiskey_token)

    db.session.add(whiskey)
    db.session.commit()

    response = whiskey_schema.dump(whiskey)
    return jsonify(response)

@api.route('/whiskey', methods = ['GET'])
@token_required
def get_whiskey(current_user_token):
    a_user = current_user_token.token
    whiskey = Whiskey.query.filter_by(whiskey_token = a_user).all()
    response = whiskeys_schema.dump(whiskey)
    return jsonify(response)

@api.route('/whiskey/<id>', methods = ['POST', 'PUT'])
@token_required
def update_whiskey(current_user_token, id):
    whiskey = Whiskey.query.get(id)
    whiskey.whiskey_name = request.json['whiskey_name']
    whiskey.whiskey_brand = request.json['whiskey_brand']
    whiskey.whiskey_location = request.json['whiskey_location']
    whiskey.whiskey_price = request.json['whiskey_price']
    whiskey.whiskey_token = current_user_token.token

    db.session.commit()
    response = whiskey_schema.dump(whiskey)
    return jsonify(response)

@api.route('/whiskey/<id>', methods = ['DELETE'])
@token_required
def delete_whiskey(current_user_token, id):
    whiskey = Whiskey.query.get(id)
    db.session.delete(whiskey)
    db.session.commit()
    response = whiskey_schema.dump(whiskey)
    return jsonify(response)