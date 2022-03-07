# How to set environment and run this app

 
 [**Link to Flask documentation**](https://flask.palletsprojects.com/en/2.0.x/)
 
 [**Link to MongoDB installation**](https://www.mongodb.com/try/download/community)
 

 ## How to install virtual environment:
 
 ```
 python -m venv
 ```
 
 ## How to run Flask:
 
 
 ### Install Flask in python virtual environment
 
 ```
 python -m pip install flask
  ```


 
 ### How to activate virtual environment:
 
 ```
 path\name\scripts\activate
 ```

### Install Flask enxtension for MongoDb

```
pip install flask-mongoengine
```

### Flask Security Extension and Flask WTF

```
pip install flask-wtf flask-security

```

 
 ### Run this commands in active virtual environment:
 
 ```bash 
 SET FLASK_APP=python_file.py
 
 SET FLASK_ENV=development 
 
 flask run
 ```
 
 ### How to run this app
 
 ```
 flask run
 ```


 
## To check all packeges installed:

```
pip freeze > requirements
```

## Sessions and authentication

Used ***Flask-Session Extension.*** The implementation is on top of the cookies and it also signs the cookies cryptographically, so it makes it very secure.

Another way to do it is Flask Login. Flask login has more interaction with database, it connects directly to the database, so data comes directly to the backhend and front-end.

To make Secret_Key secure use :
```
py -c "import os; print(os.urandom(16))"
```

## Install Flask-RESTx extension

```
pip install flask-restx
```












