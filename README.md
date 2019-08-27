# RestfulAPI-PartialCards-CloudProject
My first App Engine application is written in Python using flask that will expose RESTful API handlers allowing for linking partial credit cards to customers. A pdf file with usage examples is provided.

# Scope of the task
The application should expose two HTTP API handlers:
1. PUT handler that will accept partial credit card and customer information in JSON and store it.
2. GET handler that will return matching customers in JSON given partial details of a credit card.

# Testing
Postman - REST Client will allow you to interact with your API handlers without a GUI

# Installation

https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env

# How to run the API
To use this template, your computer needs:

1. Python 2 or 3
2. Flask (pip install flask)
3. Browse in the folder (e.g. using cmd)
4. Running the app, type "python app.py" (e.g. in cmd)
5. Browse to the IP which the console shows
6. Run Postman and use the options: Body -> raw -> JSON(application/json)
7. Use the link:  "which IP the console shows"/customer/"the trailing digits of user's credit card"

   For example: http://localhost:5000/customer/"2416" or http://localhost:8080/customer/"2416"


# Video link
https://youtu.be/xfcRV6PbOOg

# Part 2 - API Client
You can find its API client here:
https://github.com/giwrgosftw/C-API-Client-PartialCards-CloudProject
