[![License](http://img.shields.io/:license-apache-blue.svg?style=flat-square)](http://www.apache.org/licenses/LICENSE-2.0.html)
[![PyPI Downloads] (http://img.shields.io/pypi/dm/django-reset-migrations.svg)](https://pypi.python.org/pypi/django-reset-migrations)


# Django reset migrations

Add one command to reset the django migrations.

Sometimes you have one app that had a lot migrations in development process.
And this migrations could be deleted, because anybody will need this in the future.

Soo, could be stressfull delete the files, reset the database and create the first
migration again ... to start to developer again and bla bla bla ...

Because this, I made this command to reset the migrations and start the first migration.

I hope be usefull to you 2 :D

# Features

* delete migrations files
* delete registers in django_migrations
* recreate the first migrations
* apply fake migration
* delete register without delete files with --cached


## To install

```
    pip install django-reset-migrations
```

Install package in your INSTALL_APPS


```
settings.py

INSTALL_APPS = (
    ...
    'reset_migrations',
    .....
)
```

## Usage


```
    python manage.py reset_migrations crm

    or

    python manage.py reset_migrations app1 app2

    or

    python manage.py reset_migrations app1 app2 --cached
```


## Options

**--cached**:  Don´t delete the migrations files in apps
