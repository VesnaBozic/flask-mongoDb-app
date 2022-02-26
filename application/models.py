import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash

#we are creating classes (collections) for database
class User(db.Document):
    user_id     =   db.IntField( unique=True )
    first_name  =   db.StringField( max_length=50 )
    last_name   =   db.StringField( max_length=50 )
    email       =   db.StringField( max_length=30, unique=True )
    password    =   db.StringField(  )


    # we pass password to this setter and it will hash it
    # “hashed” it means it has been turned into a scrambled representation of itself
    def set_password(self, password):
        self.password = generate_password_hash(password)

    #this function will unhash password
    def get_password(self, password):
        return check_password_hash(self.password, password)

class Course(db.Document):
    course_id   =   db.StringField( max_length=10, unique=True )
    title       =   db.StringField( max_length=100 )
    description =   db.StringField( max_length=255 )
    credits     =   db.IntField()
    term        =   db.StringField( max_length=25 )


class Enrollment(db.Document):
    user_id     =   db.IntField()
    course_id   =   db.StringField( max_length=10 )