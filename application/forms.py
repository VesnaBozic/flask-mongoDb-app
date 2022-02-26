from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from application.models import User

# we are creating classes for Login and Register Page, to classes we are passing FlaskForm
class LoginForm(FlaskForm):
    #we use validators to make sure that fields are required
    email        =  StringField("Email", validators=[DataRequired(), Email()])
    password     =  StringField("Password", validators=[DataRequired(), Length(min=6, max=15)])
    remember_me  =  BooleanField("Remember me")
    submit       =  SubmitField("Login")


class RegisterForm(FlaskForm):
    email             =  StringField("Email", validators=[DataRequired()])
    password          =  StringField("Password", validators=[DataRequired(), Length(min=6, max=15)])
    password_confirm  =  StringField("Confirm password", validators=[DataRequired(),Length(min=6, max=15), EqualTo('password')])
    first_name        =  StringField("First name", validators=[DataRequired(),Length(min=2, max=55)]) 
    last_name         =  StringField("Last name", validators=[DataRequired(),Length(min=2, max=55)]) 
    submit            =  SubmitField("Register") 

    #function to validate email, we check if this email is already in use in database
    def validate_email(self,email):
        user = User.objects(email=email.data).first()
        if user:
            raise VallidationError("Email is already in use. Pick another one.")




