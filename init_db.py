from ext import app,db
from models import BaseModel,User,Clothes


with app.app_context():
    db.drop_all()
    db.create_all()

    admin = User(username = 'admin', password = 'admin777',role = 'admin',email='admin@example.com')
    BaseModel.create(admin)