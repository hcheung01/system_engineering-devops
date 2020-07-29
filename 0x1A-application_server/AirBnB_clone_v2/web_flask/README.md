# 0x13. Firewall

---
## Description

This project in the System engineering & DevOps ― Security series is about:
* What is a Web Framework
* How to build a web framework with Flask
* How to define routes in Flask
* What is a route
* How to handle variables in a route
* What is a template
* How to create a HTML response in Flask by using a template
* How to create a dynamic template (loops, conditions…)
* How to display in HTML data from a MySQL database

## How it compiles
To compile:
'''bash
python3 -m web <folder.file>
'''

## How it work
After compiling, open a new tab and use curl command to test URL:5000 for port

## Files
---
File|Task
---|---
0-hello_route.py, __init__.py | script that starts a Flask web application listening on 0.0.0.0, port 5000
1-hbnb_route.py | web application with more views
2-c_route.py | web application with more views
3-python_route.py | improved web application
4-number_route.py | improved web application with more views
5-number_template.py, templates/5-number.html | web application with Jinja template and rendered
6-number_odd_or_even.py, templates/6-number_odd_or_even.html | template if else and variable
models/engine/file_storage.py, models/engine/db_storage.py, models/state.py | update/improve storage engines and state Class
web_flask/7-states_list.py, web_flask/templates/7-states_list.html | web application with template and dynamic html contents
web_flask/8-cities_by_states.py, web_flask/templates/8-cities_by_states.html | add more objects to dynamic html and templating
web_flask/9-states.py, web_flask/templates/9-states.html | web app to fetching data from the storage engine 
web_flask/10-hbnb_filters.py, web_flask/templates/10-hbnb_filters.html, web_flask/static/ | fetching data from the storage engine 

## Directories
---
Directory Name | Description
---|---
web_flask/ | main folder for all flask files
web_flask/templates/ | All HTML files
styles/ | All CSS files
images/ | All images

## Author
Heindrick Cheung