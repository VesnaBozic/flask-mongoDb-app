from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email        =  StringField("Email", validators=[DataRequired()])
    password     =  StringField("Password", validators=[DataRequired()])
    remember_me  =  BooleanField("Remember me")
    submit       =  SubmitField("Login")


class RegisterForm(FlaskForm):
    email             =  StringField("Email", validators=[DataRequired()])
    password          =  StringField("Password", validators=[DataRequired()])
    password_confirm  =  StringField("Confirm password", validators=[DataRequired()])
    first_name        =  StringField("First name", validators=[DataRequired()]) 
    last_name         =  StringField("Last name", validators=[DataRequired()]) 
    submit            =  SubmitField("Register") 


