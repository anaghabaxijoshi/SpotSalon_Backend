from flask import Flask, render_template,request, redirect, url_for, session
from sqlalchemy import create_engine,text

connection_string='mysql+mysqlconnector://root:course123@localhost/spotsalon'
engine=create_engine(connection_string, echo=True)

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
# with engine.connect() as connection:
#       connection.execute(text("create table if not exists personal_profile(id int not null primary key,fullname varchar(100), dob datetime,sex varchar(20),sexualorientation varchar(100), genderidentity varchar(100))"))
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/owner_registration')
def owner_registration():
    return render_template('owner_registration.html')

@app.route('/signin_admin')
def signin_admin():
    return render_template('signin_admin.html')

@app.route('/signin_business_account')
def signin_business_account():
    return render_template('signin_business_account.html')

@app.route('/business_profile')
def business_profile():
    return render_template('business_profile.html')

@app.route('/customer_display')
def customer_display():
    return render_template('customer_display.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

