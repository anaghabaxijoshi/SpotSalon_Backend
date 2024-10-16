from flask import Flask, render_template,request, redirect, url_for, session
from sqlalchemy import create_engine,text
from models.models import *
from datetime import datetime
# import hashlib

app = Flask(__name__)

# app.secret_key = ""
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:course123@localhost/spotsalon"
engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"], echo=True)

Base.metadata.create_all(engine, checkfirst=True)


@app.route('/', methods=['post','get'])
def index():
    msg = ''
    if request.method == 'post' and 'username' in request.form and 'pwd' in request.form:
        username = request.form['username']
        password = request.form['pwd']
        with engine.connect() as con:
            result = con.execute(text(f"select * from profile where email_id = '{username}' and password = '{password}' "))
            account = result.fetchone()
            con.commit()

        if account:
            session['loggedin'] = True
            session['id'] = account.id
            session['username'] = account.username
            msg = 'logged in successfully'
            return redirect(url_for('home_business', msg = msg))
        else:
            msg = 'incorrect username or password'
    return render_template('index.html', msg = msg)



@app.route('/registration_business', methods = ['post', 'get'])
def registration_business():
    msg = ""
    if request.method == 'post' and 'username' in request.form and 'pwd' in request.form:
        # Get the form values
        role_id = request.form['role_id']
        name = request.form['businessname']
        email = request.form['email'].lower()
        password = request.form['pwd']
        cpassword = request.form['cpwd']
        phone = request.form['phone']
        if password != cpassword:
            msg = 'password do not match'
            return render_template('registration_business.html', msg = msg )
        with engine.connect() as con:
            result = con.execute(text(f"select * from profile where email_id == '{email}' and password == '{password}' "))
            account = result.fetchone()
            con.commit()

            if account:
                msg = 'account already exists'
                return render_template('registration_business.html', msg = msg)
            else:
                #insert the user into database
                con.execute(text(f"insert into profile (role_id, name, email_id, password, phone) values( '{role_id}', '{name}', '{email}', '{password}', '{phone}' )"))
                con.commit()
            msg = 'account created successfully'
            return redirect(url_for('home_business', msg=msg))
    return render_template('registration_business.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/signin_business_account', methods = ['get', 'post'])
def signin_business_account():
    msg = ''
    if request.method == 'post' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        with engine.connect() as con:
            result = con.execute(text(f"select * from profile where email_id = '{username}' and password = '{password}' "))
            account = result.fetchone()
            con.commit()

        if account:
            session['loggedin'] = True
            session['id'] = account.id
            session['username'] = account.username
            msg = 'logged in successfully'
            return redirect(url_for('home_business', msg = msg))
        else:
            msg = 'incorrect username or password'
    return render_template('signin_business_account.html', msg = msg)

@app.route('/signin_admin', methods = ['get', 'post'])
def signin_admin():
    msg = ''
    if request.method == 'post' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        with engine.connect() as con:
            result = con.execute(text(f"select * from profile where email_id = '{username}' and password = '{password}' "))
            account = result.fetchone()
            con.commit()

        if account:
            session['loggedin'] = True
            session['id'] = account.id
            session['username'] = account.username
            msg = 'logged in successfully'
            return redirect(url_for('home_admin', msg = msg))
        else:
            msg = 'incorrect username or password'
    return render_template('signin_admin.html', msg = msg)

@app.route('/home_business', methods = ['get', 'post'])
def home_business():
    return render_template('home_business.html')

@app.route('/home_admin', methods = ['get', 'post'])
def home_admin():
    return render_template('home_admin.html')

@app.route('/customer_display', methods= ['get','post'])
def customer_display():
    return render_template('customer_display.html')


# This page will feature a form for updating the business account, 
# including contact information and options to select the various services offered by the business.

# @app.route('/home_business', methods = ['get', 'post'])
# def home_business():
#     msg = ''
#     if request.method == 'post' and 'businessname' in request.form:
#         spot_it = request.form 




if __name__ == '__main__':
    app.run(port=8080, debug=True)
