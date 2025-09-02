from flask_wtf import FlaskForm
from wtforms.fields import (StringField,SubmitField,EmailField,TextAreaField,PasswordField,FileField,IntegerRangeField,IntegerField)
from wtforms.validators import DataRequired,length,equal_to
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    
    username = StringField("Choose a Username",validators=[DataRequired(), length(min=8,max=64)])
    email = EmailField('Enter Your Email',validators=[DataRequired()])
    password = PasswordField('Create a Password',validators=[DataRequired(), length(min=8,max=64)])
    confirmPassword = PasswordField('Repeat Your Password',validators=[DataRequired(), equal_to('password') ])
    
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    
    email = EmailField('Enter Your Email',validators=[DataRequired()])
    password = PasswordField('Enter Your Password',validators=[DataRequired(), length(min=8,max=64)])
    
    submit = SubmitField('Login')

class ClothesForm(FlaskForm):
    name=StringField("Enter a name",validators=[DataRequired(), length(min=8,max=64)])
    condition = StringField("choose a condition from 1 to 10",validators=[DataRequired(), length(min=1,max=2)])
    Clothtype = StringField("Enter a type (shirt/jeans/hat/)",validators=[DataRequired(), ])
    price= StringField("Enter $Price ",validators=[DataRequired(), length(min=1,max=32)])
    image1 = FileField('Product Image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg', 'gif'], 'Images only!')])
    image2 = FileField('Product Image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg', 'gif'], 'Images only!')])
    image3 = FileField('Product Image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg', 'gif'], 'Images only!')])
    image4 = FileField('Product Image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg', 'gif'], 'Images only!')])
    
    submit = SubmitField('Upload')
