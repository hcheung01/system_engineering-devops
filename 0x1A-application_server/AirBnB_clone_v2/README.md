# HBNB

This is the console /command interpreter for the codingschool Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON.

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

To start, navigate to the project folder and enter `./console.py` in the shell.

#### Create
`create <class name>`
Ex:
`create BaseModel`

#### Show
`show <class name> <object id>`
Ex:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Ex:
`all` or `all State`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`

## Original Author
* Kevin Yook
-----------------

# Airbnb Clone v2

## Purpose and Learning Objective
* Unit testing and how to implement it in a large project
* *args and how to use it
* **kwargs and how to use it
* How to handle named arguments in a function
* How to create a MySQL database
* How to create a MySQL user and grant it privileges
* Object Relational Mapping
* Mapping a Python Class to a MySQL table
* How to handle 2 different storage engines with the same codebase
* Using environment variables
* improve original console
* adding a Database storage engine

## What we used
* MySQL 5.7x
* SQLAlchemy version 1.2.x
* Python3 and modules
* Python unittesting
* environmental variables

## All files and directories
```bash
├── 0-setup_web_static.sh
├── 1-pack_web_static.py
├── 2-do_deploy_web_static.py
├── 3-deploy_web_static.py
├── AUTHORS
├── console.py
├── models
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── db_storage.py
│   │   ├── file_storage.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
├── README.md
├── setup_mysql_dev.sql
├── setup_mysql_test.sql
├── tests
│   ├── __init__.py
│   ├── test_console.py
│   └── test_models
│       ├── __init__.py
│       ├── test_amenity.py
│       ├── test_base_model.py
│       ├── test_city.py
│       ├── test_engine
│       │   ├── __init__.py
│       │   ├── __pycache__
│       │   │   ├── __init__.cpython-36.pyc
│       │   │   └── test_file_storage.cpython-36.pyc
│       │   └── test_file_storage.py
│       ├── test_place.py
│       ├── test_review.py
│       ├── test_state.py
│       └── test_user.py
├── versions
│   ├── web_static_20190116085331.tgz
│   ├── web_static_20190116085350.tgz
│   ├── web_static_20190116085410.tgz
│   ├── web_static_20190116085448.tgz
│   ├── web_static_20190116085713.tgz
│   └── web_static_20190116085717.tgz
└── web_static
    ├── 0-index.html
    ├── 1-index.html
    ├── 2-index.html
    ├── 3-index.html
    ├── 4-index.html
    ├── 5-index.html
    ├── 6-index.html
    ├── 7-index.html
    ├── 8-index.html
    ├── images
    │   ├── icon_bath.png
    │   ├── icon_bed.png
    │   ├── icon_group.png
    │   ├── icon.png
    │   └── logo.png
    ├── README.md
    └── styles
        ├── 2-common.css
        ├── 2-footer.css
        ├── 2-header.css
        ├── 3-common.css
        ├── 3-footer.css
        ├── 3-header.css
        ├── 4-common.css
        ├── 4-filters.css
        ├── 5-filters.css
        ├── 6-filters.css
        ├── 7-places.css
        └── 8-places.css

10 directories, 67 files
```

## Authors
* Heindrick Cheung
* Brent Janski