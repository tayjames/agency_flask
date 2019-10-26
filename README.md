# Agency

Agency was a 4 person, 10 day project built to.....(TEXT COMING SOON!)
https://git.heroku.com/the-agency-app.git
### Schema
pic here

### Initial Setup
to pry: import ipdb; ipdb.set_trace()

### Running Locally
<!-- pipenv install flask_migrate
pipenv install alembic
pipenv install Flask-Script
pipenv install Flask-SQLAlchemy
pipenv install psycopg2 -->

create the migration repository for microblog by running ```flask db init```
migrate the db by running ```flask db migrate``` then ```flask db upgrade```. To reverse any migrations, use ``` flask db downgrade```.
heroku run python manage.py migrate
>> python
>> from app import db
>> db.create_all()

### Run Tests

### Tech Stack
Language: Python v3.8.0
Framework: Flask

Dependencies:
SQLAlchemy--sql
Flask-migrate


### Installation
install python 3
pip3 install pipenv
pipenv shell
pipenv install flask
pipenv install flask-sqlalchemy
pipenv install flask-marshmallow
pipenv install marshmallow-sqlalchemy
