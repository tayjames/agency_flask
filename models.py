from manage import db,app

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
