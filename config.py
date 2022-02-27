#this is configuration module to store some major configurations that
# we use across the application

import os

#we are going to put all our configurations in a class
# and then we can access all these properties throught this class Config
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "b'7=\xc3\xc4\xb5\x85\xf4r\xb2\x8b\x9b}\x01\xdb\x87\xce"
    #SECERET KEY is a special key that is used as signature key to make sure that anything we sent across the server is not being altered

    MONGODB_SETTINGS = { 'db' : 'Flask'}