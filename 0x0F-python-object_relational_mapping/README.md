# 0x0F. Python - Object-relational mapping
---
## Description

This project in the High Level Programming series is about:
* Connecting to a MySQL database from a Python script
* How to use SELECT rows in a MySQL table from a Python script
* How to use INSERT rows in a MySQL table from a Python script
* What ORM means
* Mapping a Python Class to a MySQL table

## Languages and Technologies used
Python3 and scripting
MySQL
MySQLdb
SQLAlchemy

## Files
---
File|Task
---|---
0-select_states.py | script that lists all states from database
1-filter_states.py | script that lists all states with a name from database
2-my_filter_states.py | script that takes in an argument and displays all values in a table
3-my_safe_filter_states.py | script that takes in arguments and displays all values
4-cities_by_state.py | script that lists all cities from the database
5-filter_cities.py | script that takes in the name of a state as an argument and lists all cities of that state
model_state.py | python file that contains the class definition of a State and an instance Base = declarative_base()
7-model_state_fetch_all.py | script that lists all State objects from the database 
8-model_state_fetch_first.py | script that prints the first State object from the database 
9-model_state_filter_a.py | script that lists all State objects that contain the letter a from the database
10-model_state_my_get.py | script that prints the State object with the name passed as argument
11-model_state_insert.py | script that adds the State object “Louisiana” to the database 
12-model_state_update_id_2.py | script that changes the name of a State object from the database 
13-model_state_delete_a.py | script that deletes all State objects with a name containing the letter...
model_city.py, 14-model_city_fetch_by_state.py | classes definition

## Directories
---
Directory Name | Description
---|---
0x0F-python-object_relational_mapping | Main folder with all Python files

## Author
Heindrick Cheung