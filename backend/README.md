PostgreSQL Set-Up
-----------------
In order to use the backend scripts to create a postgres table and access it, a few steps need to take place.

1. Postgresql is installed
```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```
2. Create a user that has read and write access to database.
3. Create database for table to reside in.
```
createdb DATABASE_NAME
```
4. Log into psql and enable fuzzy matching.
```
psql -U user -c 'CREATE EXTENSION fuzzystrmatch;'
```
5. Store psql password and database name as environment variables in ~/.bashrc
```
export DB=DATABASE_NAME
export PASSWORD=PASSWORD
```
other secrets can be stored here (i.e. table name, api key, etc)

Backend Set-Up
--------------
Assuming python and pip are already installed. If they are not, install them now. Python 2.7 and Python 3 should both work.
Once done, run the following command.
```
pip install -r requirements.txt
```

Frontend Set-Up
---------------
Install:
* nvm
* npm
* webpack
* babel-core
* babel-loader
* babel-preset-es2015
* babel-preset-react
* react
* react-dom
* create-react-app
* google-maps-react

To work on a virtual environment
--------------------------------
```
pip install virtualenv
pip install virtualenvwrapper
export WORKON_HOME=~/Envs
source PATH/TO/bin/virtualenvwrapper.sh
```

Will only need to run this command once.
```
mkvirtualenv ENV
```

To use virtual environment:
```
workon ENV
```
NOTE - you will need to do this for each terminal you have open. If you are having trouble getting the workon command to work, try running the export and source commands again.



Google Maps
-----------
In order to get Google Maps to show, place the apikey in the "APIKEYHERE" spot in /templates/cities.html line 60.


Go Time
-------
Results ran best on Firefox. Ran into some encoding issues with alternate names in Chrome so switched to Firefox.

To run tests:
```
python manage.py test
```

To run repo:
```
python manage.py runserver
```

Access Exact Resource:
```
localhost:5000/cities/CITY NAME
```

Access Fuzzy Matching Resource:
```
localhost:5000/cities?like=CITY NAME
```

Front End Resources:
```
localhost:5000/
localhost:5000/cities
```

Resources
---------
PostgreSQL set-up - https://wiki.postgresql.org/wiki/First_steps
