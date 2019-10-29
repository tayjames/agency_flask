# Agency

Agency was a 4 person, 13 day project built to connect clients with physical limitations with volunteers willing to help out. Users choose whether or not they are a client or a volunteer, and upon account creation have the ability to either pick up volunteer opportunities, or create them. Users and Opportunities have full CRUD functionality.


[Backend](https://git.heroku.com/the-agency-app.git)
[Frontend]()

### Schema
![Schema](/images/schema.png)

### Initial Setup
$ git clone git@github.com:tayjames/agency_flask.git
$ cd agency_flask
$ install python3
$ pip3 install pipenv
$ pipenv shell
$ pipenv install flask
$ pipenv install flask-sqlalchemy
$ pipenv install flask-marshmallow
$ pipenv install marshmallow-sqlalchemy
$ pipenv install flask_migrate
$ pipenv install alembic
$ create the migration repository for microblog by running ```flask db init```
$ migrate the db by running ```flask db migrate``` then ```flask db upgrade```.
$ To reverse any migrations, use ``` flask db downgrade```.


### Run Tests

### Helpful Code
to pry: ``` import ipdb; ipdb.set_trace()```




### Tech Stack
Language: Python v3.8.0
Framework: Flask

Dependencies:
SQLAlchemy--sql
Flask-migrate
