from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
import secrets 

login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(150), nullable=True, default='')
    last_name = db.Column(db.String(150), nullable=True, default='')
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String, nullable=True, default='')
    g_auth_verify = db.Column(db.Boolean, default=False)
    token = db.Column(db.String, default='', unique=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow )

    def __init__(self, email, first_name='', last_name='', password='', token='', g_auth_verify=False):
        self.id = self.set_id()
        self.first_name = first_name 
        self.last_name = last_name 
        self.password = self.set_password(password)
        self.email = email 
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)
    
    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f'{self.email} has been added!'

class Whiskey(db.Model):
    id = db.Column(db.String, primary_key=True)
    whiskey_name = db.Column(db.String(100), nullable=False)
    whiskey_brand = db.Column(db.String(100), nullable=False)
    whiskey_location = db.Column(db.String(100), nullable=False)
    whiskey_price = db.Column(db.Float(precision=2))
    whiskey_token = db.Column(db.String, db.ForeignKey('user.token'), unique=True)

    def __init__(self, whiskey_name, whiskey_brand, whiskey_location, whiskey_pice, whiskey_token, id=''):
        self.id = self.set_id()
        self.whiskey_name = whiskey_name 
        self.whiskey_brand = whiskey_brand 
        self.whiskey_location = whiskey_location
        self.whiskey_price = whiskey_pice
        self.whiskey_token = whiskey_token

    def __repr__(self):
        return f'The following Whiskeys have been added to your inventory: {self.whiskey_name}'
    
    def set_id(self): 
        return (secrets.token_urlsafe())

class WhiskeySchema(ma.Schema):
    class Meta: 
        fields = ['id', 'whiskey_name', 'whiskey_brand', 'whiskey_location', 'whiskey_price']

whiskey_schema = WhiskeySchema()
whiskeys_schema = WhiskeySchema(many=True)
