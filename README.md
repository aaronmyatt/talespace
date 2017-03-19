
# Talespace
Talespace NGO website API

## Setting up Development Enviornmet

* Clone the repo `https://github.com/aaronmyatt/talespace-backend.git`
* Make your Virtualenv either
    * Vitualenv
        * `virtualenv env_name -p python3`
    * Conda
        * `conda-env create -f env.yaml`
* install dependencies with using `pip install -r requirements.txt`

#### Setting up the Database

 * Ubuntu 16.04

    * install Mariadb server and client `sudo apt-get install mariadb-client mariadb-server` / `brew install mariadb`
    *if on linux:*
    * install `sudo apt-get install libmysqlclient-dev`

### DB Configuration

Run `sudo mysql -u root` then create database and user

```
CREATE DATABASE talespace CHARACTER SET UTF8;
CREATE USER talespaceuser@localhost IDENTIFIED BY '123';
GRANT ALL PRIVILEGES ON talespace.* TO talespaceuser@localhost;
FLUSH PRIVILEGES;
```

### Django Configuration

Change database settings in your setting file

```Python
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'talespace',
        'USER': 'talespaceuser@localhost',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '',
    }
```

### Django ORM Migrations

Load all Django app models. From the root of the app run:
`./manage.py makemigrations`
`./manage.py migrate`

### Runserver
`./manage.py runserver`
