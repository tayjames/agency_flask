# Agency

Agency was a 4 person, 13 day project built to connect clients with physical limitations with volunteers willing to help out. Users choose whether or not they are a client or a volunteer, and upon account creation have the ability to either pick up volunteer opportunities, or create them. Users and Opportunities have full CRUD functionality. Take a look below to see the endpoints you can access and examples of successful requests and responses.


[Backend](https://git.heroku.com/the-agency-app.git)

[Frontend]()

### Schema
![Schema](/images/schema.png)

### Initial Setup
* $ git clone git@github.com:tayjames/agency_flask.git   
* $ cd agency_flask   
* $ install python3 from python.org  
* $ pip3 install pipenv   
* $ pipenv shell   
* $ pipenv install flask   
* $ pipenv install flask-sqlalchemy   
* $ pipenv install flask-marshmallow   
* $ pipenv install marshmallow-sqlalchemy    
* $ pipenv install flask_migrate   
* $ pipenv install alembic   
* $ create the migration repository for microblog by running ```flask db init```     
* $ migrate the db by running ```flask db migrate``` then ```flask db upgrade```     
* $ To reverse any migrations, use ``` flask db downgrade```     


### Run Locally
* Run ```flask run```
* Open a window to http://localhost:5000 or postman and enter an endpoint

### Run Tests
<coming soon!>

### Helpful Code
to pry: ``` import ipdb; ipdb.set_trace()```

### User Endpoints

* Create a User
```
POST https://the-agency-app.herokuapp.com/user 
send in a body that looks like this: 
{
    "email": "ba@example.com",
    "first_name": "barack",
    "id": 18,
    "last_name": "obama",
    "password": "$2b$12$qq2WmLt8eL6NaiNSsw6rG.FHc2Pm6D6ClvyjHZSqHLOwuqVazQ0pu",
    "phone_number": 123456789,
    "role": "volunteer"
}

RESPONSE: 
{
    "email": "ba@example.com",
    "first_name": "barack",
    "id": 18,
    "last_name": "obama",
    "password": "$2b$12$qq2WmLt8eL6NaiNSsw6rG.FHc2Pm6D6ClvyjHZSqHLOwuqVazQ0pu",
    "phone_number": 123456789,
    "role": "volunteer"
}, 201
```

* Update User Information
```PUT https://the-agency-app.herokuapp.com/users/<user_id>  ```
send with first_name, last_name, password, email, phone_number in the body

204 NO CONTENT

* Show All Users
```
GET https://the-agency-app.herokuapp.com/users 

[
    {
        "email": "tj@example.com",
        "first_name": "Thomas",
        "id": 1,
        "last_name": "Jefferson",
        "password": "$2b$12$Ll2Chr2I3jCSoiVKyaWbzOXM.WnUtbLgdNPPp1BDqNl7XxQTke2Tq",
        "phone_number": 1234567890,
        "role": "volunteer"
    },
    {
        "email": "wg@example.com",
        "first_name": "William",
        "id": 2,
        "last_name": "Garfield",
        "password": "$2b$12$Ll2Chr2I3jCSoiVKyaWbzOXM.WnUtbLgdNPPp1BDqNl7XxQTke2Tq",
        "phone_number": 1234567890,
        "role": "client"
    },
    {
        "email": "al@example.com",
        "first_name": "Abraham",
        "id": 3,
        "last_name": "Lincon",
        "password": "$2b$12$j7tSUsUpPfNGaDMf8bjasOoXuUSOPtQeWvqmpa8i.Yc2YltxrjBam",
        "phone_number": 1234567890,
        "role": "volunteer"
    } ...
```



* Show Single User
```
GET https://the-agency-app.herokuapp.com/user/<user_id>

{
        "email": "al@example.com",
        "first_name": "Abraham",
        "id": 3,
        "last_name": "Lincon",
        "password": "$2b$12$j7tSUsUpPfNGaDMf8bjasOoXuUSOPtQeWvqmpa8i.Yc2YltxrjBam",
        "phone_number": 1234567890,
        "role": "volunteer"
    }
```

* Delete a User
```DELETE https://the-agency-app.herokuapp.com/<user_id>

  204 NO CONTENT
```

* User Login
``` POST https://the-agency-app.herokuapp.com/login ```

### Opportunity Endpoints

* Create an Opportunity
```
POST https://the-agency-app.herokuapp.com/users/<user_id>/opportunity

[
    {
        "description": "I cannot rake my yard- I need someone to come in and get the front and back yard.",
        "estimated_time": "1 hr",
        "location": "2848 Roslyn St., Denver CO 80238",
        "title": "Rake Leaves",
        "type": "Physical Labor"
        }
]

```

* Update an Opportunity
```PUT https://the-agency-app.herokuapp.com/users/<user_id>/opportunity/<opportunity_id> 

send with title, type, description, location and estimated time attributes in the body

```

* Show All Opportunities
```
GET https://the-agency-app.herokuapp.com/opportunities 

[
    {
        "description": "I cannot rake my yard- I need someone to come in and get the front and back yard.",
        "estimated_time": "1 hr",
        "fulfilled": true,
        "id": 2,
        "location": "2848 Roslyn St., Denver CO 80238",
        "title": "Rake Leaves",
        "type": "Physical Labor",
        "user_id": 1
    },
    {
        "description": "Need a ride to a concert, cannot drive myself.",
        "estimated_time": "30 min",
        "fulfilled": true,
        "id": 4,
        "location": "2848 Roslyn St., Denver CO 80238",
        "title": "Need Ride",
        "type": "Transportation",
        "user_id": 15
    },
    {
        "description": "Need help getting groceries",
        "estimated_time": "30 min",
        "fulfilled": null,
        "id": 5,
        "location": "2848 Roslyn St., Denver CO 80238",
        "title": "Carry Groceries",
        "type": "Chore",
        "user_id": 5
    }
```

* Show Single Opportunity for one User
```
GET https://the-agency-app.herokuapp.com/users/<user_id>/opportunity/<opportunity_id>  

[
    {
        "description": "I cannot rake my yard- I need someone to come in and get the front and back yard.",
        "estimated_time": "1 hr",
        "fulfilled": true,
        "id": 2,
        "location": "2848 Roslyn St., Denver CO 80238",
        "title": "Rake Leaves",
        "type": "Physical Labor",
        "user_id": 1
    }
]

```

* Delete an Opportunity
```DELETE https://the-agency-app.herokuapp.com/users/<user_id>/opportunity/<opportunity_id>

204 NO CONTENT
```

### Opportunity Reservation Endpoint
* ```

POST https://theagencyapp.herokuapp.com/users/<volunteer_id>/opportunities/<opportunity_id>

{
    "id": 3,
    "opportunity_id": 4,
    "volunteer_id": 2
}

hitting this endpoint will also update opportunity fulfilled attribute to true, which is defaulted to false upon creation.
```

### Tech Stack
* Language: Python v3.8.0
* Framework: Flask

Dependencies:
* SQLAlchemy--sql
* Flask-migrate



### Core Contributors:

* [Tay James](https://github.com/tayjames)
* [Greg Anderson](https://github.com/gregoryanderson)
* [Aiden McKay](https://github.com/JellyBeans1312)
* [Mills Provosty](https://github.com/MillsProvosty)
