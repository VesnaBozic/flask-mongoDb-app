# About Flask

 
 [**Link to Flask documentation**](https://flask.palletsprojects.com/en/2.0.x/)
 
 ## What is Flask?
 
Flask is a web microframework, it’s a Python module that lets you develop web applications. It’s doesn’t include an ORM (Object Relational Manager).Flask has a built-in server that will allow us to turn our Python scripts into webpages and web apps. Flask allows us to make websites with Python. 
 
 ## How to install virtual environment:
 
 > **python -m venv**
 
 ## How to run Flask:
 
 ### Install Flask in python virtual environment
 
 > **python -m pip install flask**
 
 ### How to activate virtual environment:
 
 > **path\name\scripts\activate**
 
 ### Run this commands in active virtual environment:
 ```bash 
 SET FLASK_APP=python_file.py
 
 SET FLASK_ENV=development 
 
 flask run
 ```
 
 # Flask app
 
 ![hello world](/assets/img/hello.jpg)
 
 In this code snippet we see small Flask application. 
 ``` 
 app = Flask(__name__)
 ```
 
 First we import Flask class and then create the application instace of class Flask.
 
 **__name__** variable passed to the Flask class is a Python predefind variable and it configures FLask in the correct way. This is needed so that Flask knows where to look for resources such as templates and static files.
 
 **the routes** are the different URLs that the application implements
 
 In Flask, handlers for the application routes are written as Python functions, called **view functions**
  
 @app.route('/') will leads us on the main page of application


**@app.route** is decorator, a unique function of the Python language
A decorator modifies the function that follows it.

the @app.route decorator creates an association between the URL given as an argument and the function.
-route() decorator will tell Flask what URL should trigger our function.

The function returns the message we want to display in the user’s browser. The default content type is HTML, so HTML in the string will be rendered by the browser.
