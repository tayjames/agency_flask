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


### Run Locally
* Run ```flask run```
* Open a window to http://localhost:5000 or postman and enter an endpoint

### Run Tests
<coming soon!>

### Helpful Code
to pry: ``` import ipdb; ipdb.set_trace()```

### User Endpoints

* Create a User
```POST https://the-agency-app.herokuapp.com/user ```

* Update User Information
```PUT https://the-agency-app.herokuapp.com/users/<user_id>  ```

* Show All Users
```GET https://the-agency-app.herokuapp.com/users ```

* Show Single User
```GET https://the-agency-app.herokuapp.com/user/<user_id>  ```

* Delete a User
```DELETE https://the-agency-app.herokuapp.com/<user_id>  ```

* User Login
``` POST https://the-agency-app.herokuapp.com/login ```

### Opportunity Endpoints

* Create an Opportunity
```POST https://the-agency-app.herokuapp.com/users/<user_id>/opportunity  ```

* Update an Opportunity
```PUT https://the-agency-app.herokuapp.com/users/<user_id>/opportunity/<opportunity_id>  ```

* Show All Opportunities
```GET https://the-agency-app.herokuapp.com/opportunities  ```

* Show Single Opportunity for one User
```GET https://the-agency-app.herokuapp.com/users/<user_id>/opportunity/<opportunity_id>  ```

* Delete an Opportunity
```DELETE https://the-agency-app.herokuapp.com/users/<user_id>/opportunity/<opportunity_id>  ```

### Opportunity Reservation Endpoint
```POST https://the-agency-app.herokuapp.com/users/<volunteer_id>/opportunities/<opportunity_id>```

### Tech Stack
Language: Python v3.8.0
Framework: Flask

Dependencies:
SQLAlchemy--sql
Flask-migrate



### Core Contributors:

* [Tay James](https://github.com/tayjames)
* [Greg Anderson](https://github.com/gregoryanderson)
* [Aiden McKay](https://github.com/JellyBeans1312)
* [Mills Provosty](https://github.com/MillsProvosty)
