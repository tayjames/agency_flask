from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from datetime import datetime
import os
import bcrypt

# init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# init db
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# init marshmallow
ma = Marshmallow(app)

# User Class/model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    phone_number= db.Column(db.Integer)
    opportunities = db.relationship('Opportunity', backref='client')

    def __init__(self, first_name, last_name, email, password, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone_number = phone_number

class Opportunity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    type = db.Column(db.String(120), index=True)
    location = db.Column(db.String(120), index=True)
    estimated_time = db.Column(db.String(120), index=True)
    description = db.Column(db.String(140), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, type, location, estimated_time, description, user_id):
        self.title = title
        self.type = type
        self.location = location
        self.estimated_time = estimated_time
        self.description = description
        self.user_id = user_id

# USER Schemas
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'phone_number')

# OPPORTUNITY Schemas
class OpportunitySchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'type', 'location', 'estimated_time', 'description', 'user_id')

# Init Schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)
opportunity_schema = OpportunitySchema()
opportunities_schema = OpportunitySchema(many=True)

#create a User
@app.route('/user', methods=['POST'])
def create_user():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    # import ipdb; ipdb.set_trace()

    password = bcrypt.hashpw(request.json['password'].encode('utf8'), bcrypt.gensalt())
    phone_number = request.json['phone_number']

    new_user = User(first_name, last_name, email, password, phone_number)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

# Get single user
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    # import ipdb; ipdb.set_trace()
    return user_schema.jsonify(user)

# Update a user
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)

    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    phone_number = request.json['phone_number']

    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.phone_number = phone_number

    db.session.commit()

    return user_schema.jsonify(user)

# Delete single user
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)

# Create an Opportunity
@app.route('/users/<user_id>/opportunity', methods=['POST'])
def create_opportunity(user_id):
    title = request.json['title']
    type = request.json['type']
    location = request.json['location']
    estimated_time = request.json['estimated_time']
    description = request.json['description']
    user_id = request.json['user_id']

    new_opportunity = Opportunity(title, type, location, estimated_time, description, user_id)

    db.session.add(new_opportunity)
    db.session.commit()

    return opportunity_schema.jsonify(new_opportunity)


# run server
if __name__ == '__main__':
    app.run(debug=True)
