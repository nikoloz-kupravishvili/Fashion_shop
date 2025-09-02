from flask import render_template,redirect,flash,request,url_for
from forms import RegisterForm,LoginForm,ClothesForm
from werkzeug.utils import secure_filename
from ext import app,db,login_manager
from models import BaseModel,User,Clothes
from flask_login import login_user , logout_user, login_required,current_user
import os

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/admin', methods=['GET', 'POST'])
@login_required
def upload():
    form = ClothesForm()
    if form.validate_on_submit():
        name = form.name.data
        condition =  form.condition.data
        price = form.price.data
        Clothtype = form.Clothtype.data

        image1 = form.image1.data
        filename1 = secure_filename(image1.filename)
        image1.save(os.path.join(UPLOAD_FOLDER, filename1))
        
        image2 = form.image2.data
        filename2 = secure_filename(image2.filename)
        image2.save(os.path.join(UPLOAD_FOLDER, filename2))

        image3 = form.image3.data
        filename3 = secure_filename(image3.filename)
        image3.save(os.path.join(UPLOAD_FOLDER, filename3))

        image4 = form.image4.data
        filename4 = secure_filename(image4.filename)
        image4.save(os.path.join(UPLOAD_FOLDER, filename4))
        # Save filename to DB if needed

        product = Clothes(name=name, price=price, condition = condition,Clothtype = Clothtype,image_filename_1=filename1,image_filename_2=filename2,image_filename_3 = filename3,image_filename_4=filename4)
        BaseModel.create(product)
        return redirect(url_for('clothes'))
    return render_template('admin.html', form=form)

    

@app.route('/')
def home():
    return render_template('home.html',)


@app.route('/clothes')
def clothes():
    clothes = Clothes.query.all()
    return render_template('clothes.html',clothes = clothes)


@app.route('/login',methods = ['GET','POST'])
def login():
    form = LoginForm()
    
    
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter(email==User.email).first() #none
        if user and user.check_password(password): #0 ,[], None , "" -->False
            login_user(user)
            flash('Login Succesful')
            return redirect('/')
           
    return render_template("signin.html" , form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')


@app.route('/register',methods = ['GET','POST'])
def register():
    form  = RegisterForm()
    if form.validate_on_submit():
        new_user = User(
            username = form.username.data,
            email = form.email.data,
            password = form.password.data
        )
        BaseModel.create(new_user)
        flash('Registration Succesful')
        return redirect('/login')
    
    return render_template("signup.html" , form=form)



@app.route('/card/<int:product_id>')
def card(product_id):
    
    product = Clothes.query.all()
    return render_template("card.html" , product_id=product_id,prod = product[product_id-1])


@app.route('/delete-mail/<int:cloth_id>')
@login_required
def delete_email(cloth_id):
    cloth = Clothes.query.get(cloth_id)
    BaseModel.delete(cloth)
    products = Clothes.query.order_by(Clothes.id).all()
    for index, product in enumerate(products, start=1):
        product.id = index
    db.session.commit()

    # Reset auto-increment counter (SQLite-specific)
    db.session.execute("DELETE FROM sqlite_sequence WHERE name='product'")
    db.session.commit()
    return redirect('/clothes')

@app.route('/about')
def about(): 
    return render_template('about.html')



@app.route('/contact')
def contact(): 
    return render_template('contact.html')



@app.route('/cart')
def cart(): 
    return render_template('cart.html')
