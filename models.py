from ext import db ,login_manager
from sqlalchemy import ForeignKey
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash 



#class to easily add an remove objects from database
class BaseModel:
    def create(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def save():
        db.session.commit()

# create database to store registration data
class User(db.Model,BaseModel,UserMixin):
    __tablename__ = 'users'  #name of the table

    id = db.Column(db.Integer(),primary_key = True)

    username = db.Column(db.String() , nullable =False)
    email = db.Column(db.String() , nullable =False)
    password = db.Column(db.String() , nullable =False)
    role = db.Column(db.String(), nullable = False)

    def __init__(self,username,password,email,role = 'Guest'):
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role
        self.email = email


    def check_password(self,password):
         return check_password_hash(self.password,password)
    
    def __str__(self):
        return self.username  # So str(user) returns the username

    def __repr__(self):
        return f"<User {self.username}>"



class Clothes(db.Model,BaseModel):
    __tablename__ = 'clothes'  #name of the table

    id = db.Column(db.Integer(),primary_key = True)
    image_filename_1 = db.Column(db.String(200))
    image_filename_2 = db.Column(db.String(200))
    image_filename_3 = db.Column(db.String(200))
    image_filename_4 = db.Column(db.String(200))
    Clothtype = db.Column(db.String() , nullable =False)
    name = db.Column(db.String() , nullable =False)
    condition = db.Column(db.String() , nullable =False)
    price = db.Column(db.String(), nullable = False)

    def __init__(self,Clothtype,name,condition,price,image_filename_1,image_filename_2= "/static/uploads/No_Image_Available.jpg",image_filename_3= "/static/uploads/No_Image_Available.jpg",image_filename_4= "/static/uploads/No_Image_Available.jpg"):
        self.Clothtype = Clothtype
        self.name = name
        self.condition= condition
        self.price = price
        self.image_filename_1 = image_filename_1
        self.image_filename_2 = image_filename_2
        self.image_filename_3 = image_filename_3
        self.image_filename_4 = image_filename_4




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)