from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField, StringField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')


class RegisterForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Type the password again', validators=[DataRequired()])
    name = StringField('User name', validators=[DataRequired()])
    surname = StringField('User surname', validators=[DataRequired()])
    speciality = StringField("Your speciality", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    age = StringField("Your age", validators=[DataRequired()])
    position = StringField("Your position in team", validators=[DataRequired()])
    submit = SubmitField('Sign in')
