# GraphQL Sample App With Flask

This sample was created by following [this tutorial](https://www.apollographql.com/blog/complete-api-guide/)

## Project Structure

- Flask — this is the web server that we’ll use
- Flask-SQLAlchemy — an ORM that makes it easier for us to communicate with our SQL database
- Ariadne — a library for GraphQL python integration
- Flask-Cors — an extension for Cross Origin Resource Sharing

## Learning Objectives

- Set up a Python web server with Flask
- Use the Ariadne library to implement GraphQL
- Compose a GraphQL Schema
- Perform queries and mutations against a Python GraphQL API

## Project creation

```sh
mkdir graphql-python-api
cd graphql-python-api

python3 -m venv .venv
source .venv/bin/activate

pip install flask ariadne flask-sqlalchemy flask-cors
```

## Running the app

```sh
source .venv/bin/activate
flask run
```

You can use the REST and GraphQL endpoints, you can also visit the `/graphql` endpoint from your browser to use the GraphiQL IDE

## Manual DB creation

To manually create the database and add records:

in python shell

```py
from app import app, db
# create the application context
with app.app_context():
    # create the database from db
    db.create_all()
```

check with some tool if db is created successfully (I use [sqlitebrowser](https://github.com/sqlitebrowser/sqlitebrowser))

Add a few entries manually from the python shell:

```py
from datetime import datetime
from api.models import Post
current_date = datetime.today().date()
new_post = Post(title="A new morning", description="A new morning details", created_at=current_date)
with app.app_context():
    db.session.add(new_post)
    db.session.commit()
```

check again that the data is inserted successfully
