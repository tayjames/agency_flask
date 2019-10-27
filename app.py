from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS
from datetime import datetime
from errors import bad_request
import os
import bcrypt
import logging
import json

# init app
app = Flask(__name__)
CORS(app, resources=r'*', headers='Content-Type')
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
    role = db.Column(db.String(100))
    opportunities = db.relationship('Opportunity', backref='client')

    def __init__(self, first_name, last_name, email, password, phone_number, role):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.role = role

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
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'phone_number', 'role')

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
    data = request.data
    json_formatted_data = json.loads(data)

    if 'first_name' not in json_formatted_data or 'last_name' not in json_formatted_data or 'email' not in json_formatted_data or 'password' not in json_formatted_data or 'phone_number' not in json_formatted_data or 'role' not in json_formatted_data:
        return bad_request('Error: Missing Fields')
    if User.query.filter_by(email=json_formatted_data['email']).first():
        return bad_request('That email is in use, please pick another.')

    first_name = json_formatted_data['first_name']
    last_name = json_formatted_data['last_name']
    email = json_formatted_data['email']
    password = bcrypt.hashpw(json_formatted_data['password'].encode('utf8'), bcrypt.gensalt())
    phone_number = json_formatted_data['phone_number']
    role = json_formatted_data['role']

    new_user = User(first_name, last_name, email, password, phone_number, role)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user), 201


# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result), 200

# Get single user
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user), 200

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

    return user_schema.jsonify(user), 200

# Delete single user
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):

    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    all_users = User.query.all()
    return users_schema.jsonify(all_users), 204

# Create an Opportunity
@app.route('/users/<user_id>/opportunity', methods=['POST'])
def create_opportunity(user_id):
    data = request.get_json()
    if 'title' not in data or 'location' not in data or 'type' not in data or 'description' not in data or 'estimated_time' not in data:
        return bad_request('Error: Missing Fields')

    title = request.json['title']
    type = request.json['type']
    location = request.json['location']
    estimated_time = request.json['estimated_time']
    description = request.json['description']

    new_opportunity = Opportunity(title, type, location, estimated_time, description, user_id)

    db.session.add(new_opportunity)
    db.session.commit()

    return opportunity_schema.jsonify(new_opportunity), 201

# Get all opportunities for one user
# @app.route( '/users/<user_id>/opportunities>', methods=['GET'])
# def get_opportunities(user_id):
#     user = User.query.get(user_id)
#     all_opportunities = user.opportunities
#     result = opportunities_schema.dump(all_opportunities)
#     return jsonify(result), 200

# Get single opportunity for one user
@app.route('/users/<user_id>/opportunity/<id>', methods=['GET'])
def get_opportunity(user_id, id):
    user = User.query.get(user_id)
    opportunity = Opportunity.query.get(id)
    return opportunity_schema.jsonify(opportunity), 200

# Update a users opportunity
@app.route('/users/<user_id>/opportunity/<id>', methods=['PUT'])
def update_opporutnity(user_id, id):
    user = User.query.get(user_id)
    opportunity = Opportunity.query.get(id)
    title = request.json['title']
    type = request.json['type']
    location = request.json['location']
    estimated_time = request.json['estimated_time']
    description = request.json['description']

    opportunity.title = title
    opportunity.type = type
    opportunity.location = location
    opportunity.estimated_time = estimated_time
    opportunity.description = description
    opportunity.user_id = user_id

    db.session.commit()

    return opportunity_schema.jsonify(opportunity), 200

#Delete opportunity for user
@app.route('/users/<user_id>/opportunity/<id>', methods=['DELETE'])
def delete_opportunity(user_id, id):
    user = User.query.get(user_id)
    opportunity = Opportunity.query.get(id)
    db.session.delete(opportunity)
    db.session.commit()
    return opportunities_schema.jsonify(opportunities), 204


# run server
if __name__ == '__main__':
    app.run(debug=True)
