Django reset migrations
=======================

Add one command to reset the django migrations.

Sometimes you have one app that had a lot migrations in development
process. And this migrations could be deleted, because anybody will need
this in the future.

Soo, could be stressfull delete the files, reset the database and create
the first migration again ... to start to developer again and bla bla
bla ...

Because this, I made this command to reset the migrations and start the
first migration.

I hope be usefull to you 2 :D

To install
----------

::

        pip install django-reset-migrations

Install package in your INSTALL\_APPS

::

    settings.py

    INSTALL_APPS = (
        ...
        'resetmigrations',
        .....
    )

Usage
-----

::

        python manage.py reset_migration crm

        or

        python manage.py reset_migration app1 app2

        or

        python manage.py reset_migration app1 app2 --cached

Options
-------

**--cached**: Don´t delete the migrations files in apps
