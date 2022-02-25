#this is configuration module to store some major configurations that
# we use across the application/

import os

#we are going to put all our configurations in a class
# and then we can access all these properties throught this class Config
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"
    #SECERET KEY is a special key that is used as signature key to make sure that anything we sent across the server is not being altered

    MONGODB_SETTINGS = { 'db' : 'Flask'}