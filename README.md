
# Talespace
Talespace NGO website

## Setting up Development Enviornmet

* Clone the repo `https://github.com/aaronmyatt/talespace-backend.git`
* Make your Virtualenv either
    * Vitualenv
        * `virtualenv env_name -p python3`
    * Conda
        * `conda-env create -f env.yaml`
* install dependencies with pip `pip install -r requirements.txt`

#### Setting Database

 * Ubuntu 16.04

    * install Mariadb server and client `sudo apt-get install mariadb-client mariadb-server`
    * install `sudo apt-get install libmysqlclient-dev`

### DB Configuration

Run `sudo mysql -u root` then create database and user

```
CREATE DATABASE talespace CHARACTER SET UTF8;
CREATE USER talespace@localhost IDENTIFIED BY '123';
GRANT ALL PRIVILEGES ON talespace.* TO talespace@localhost;
FLUSH PRIVILEGES;
```

### Django Configuration

Change database settings in your setting file

```Python
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'boost',
        'USER': 'boostuser',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '',
    }
```
