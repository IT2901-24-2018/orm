## Setting up React and Django
We wrote this guide for Linux, some adjustments could be required for OS X and Windows. You don't _have_ to have Yarn, or virtualenvwrapper, or virtualenv, but it's all recommended.

### Frontend
Make sure you have [npm](https://nodejs.org/en/) installed through Node. You can easily test this by running `npm -v` in your terminal. We also recommend you use [Yarn](https://yarnpkg.com/lang/en/) to install packages, and our instructions will assume that you do.
Now you should be ready to install our frontend dependencies.
```
cd frontend
yarn
```

When the dependencies are finished installing, you can start up the frontend server.

`yarn start`

It will automatically open your browser at localhost:3000, but you can close that.

### Backend
While the frontend server is running in your terminal, open up another terminal to set up the backend.

We recommend setting up a virtualenv to contain the backend dependencies. [Here's](https://gist.github.com/IamAdiSri/a379c36b70044725a85a1216e7ee9a46) a solid guide on installing virtualenvwrapper for Python3. 
Make yourself a virtualenv for the project with `mkvirtualenv orm` and remember to run `workon orm` to have access to the backend dependencies.

When your virtual environment is set up, get the required dependencies for the backend:

`pip install -r requirements.txt`

### Database

[For installing Postgres with PostGIS.](http://trac.osgeo.org/postgis/wiki/UsersWikiPostGIS23UbuntuPGSQL96Apt) Then skip to "Boot up postgres user promt"

We haven't noted down instructions for Windows, but try downloading Postgres [here](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads#windows) and installing it [here](http://www.postgresqltutorial.com/install-postgresql/). The following instructions are designed for Linux and potentially OS X.

First, get the postgresql packages through apt.

`sudo apt install postgresql postgresql-contrib`

Boot up postgres user prompt

`sudo su - postgres`

You should now be in a shell session as the `postgres` user. Begin a Postgres session:

`psql`

Make the database

`CREATE DATABASE orm;`

Make a database user which will connect to and interact with the database. Remember the username and password,

`CREATE USER username WITH PASSWORD 'password';`

Give the new user permission to create databases, which is neccessary for our backend tests.

`ALTER ROLE username CREATEDB;`

Set the following connection parameters for the user we created, speeding up database operations.
```
ALTER ROLE username SET client_encoding TO 'utf8';
ALTER ROLE username SET default_transaction_isolation TO 'read committed';
ALTER ROLE username SET timezone TO 'UTC';
```

Now we need to grant the database user access rights to the database we created.

`GRANT ALL PRIVILEGES ON DATABASE orm TO username;`


Exit the SQL prompt to get back to the postgres user session.

`\q`

We're done with this user, so we can also exit the postgres user shell session, to get your regular shell back.

`exit`

Now, we have to give this information to our Django config. We start by navigating to our settings folder.

`cd backend/settings/`

Copy the local_example.py file to a local.py file, which will be hidden from git and contain your specific database information.

`cp local_example.py local.py`

Open up local.py and edit the values of "username" and "password" to the values you set earlier.

Apply the latest and greatest in database migrations:

`python manage.py migrate`

Now you can start up the backend server.

`python manage.py runserver`

The website should now be available at [localhost:8000](http://localhost:8000)

To make users for the API.

`python manage.py createsuperuser`

This is a super user. That includes staff priveleiges.

To make a normal user.

```
from django.contrib.auth.models import User

User.objects.create_user(username="username", password="password")
```

## Misc
You can run `make test` to run all our tests and lints locally.

Thanks to [Vikas Yadav](http://v1k45.com/blog/modern-django-part-1-setting-up-django-and-react/) for the React+Django setup tutorial we used.
