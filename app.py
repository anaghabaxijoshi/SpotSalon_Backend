from flask import Flask, render_template,request, redirect, url_for, session
from sqlalchemy import create_engine,text
from models.models import *
from datetime import datetime
# import hashlib

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:course123@localhost/spotsalon"
engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"], echo=True)

Base.metadata.create_all(engine, checkfirst=True)


@app.route('/', methods=['post','get'])
def index():

    msg = ''
    if request.method == 'post' and 'username' in request.form and 'pwd' in request.form:
        try:
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
        except Exception as e:
            print(e)
            return render_template('index.html', e=e)
    return render_template('index.html')



@app.route('/registration_business', methods = ['post', 'get'])
def registration_business():
    msg = ""
    if request.method == 'POST':
        try:
            # Get the form values
            role = request.form['role']
            name = request.form['businessname']
            email = request.form['email'].lower()
            password = request.form['pwd']
            cpassword = request.form['cpwd']
            if password != cpassword:
                msg = 'password do not match'
                return render_template('registration_business.html', msg = msg )
       
            #check if account already exists
            with engine.connect() as con:
                result = con.execute(text(f"select * from profile where email_id = '{email}' and password = '{password}' "))
                account = result.fetchone()
                con.commit()

                if account:
                    msg = 'Account already exists'
                    return render_template('registration_business.html', msg = msg)
                else:
                #insert the user into database
                    with engine.connect() as con:
                        con.execute(text(f"insert into profile (role, name, email_id, password) values( '{role}', '{name}', '{email}', '{password}' )"))
                        con.commit()
                        msg = 'account created successfully'
                    return render_template('home_business.html', msg=msg)
        except Exception as e:
            print(e)
            return render_template('registration_business.html', e=e)
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

# This page will feature a form for updating the business account, 
# including contact information and options to select the various services offered by the business.
# To edit Account Information
@app.route('/home_business', methods = ['get', 'post'])
def home_business():
    account = ""
    if request.method == 'POST':
        try:
            # Get the form values for table profile
            spot_id = request.form['spot_id']
            role = request.form['role']
            name = request.form['businessname']
            username = request.form['email'].lower()
            password = request.form['pwd']

            # Get the form values for table salon_contact
            phone = request.form['phone']
            city = request.form['city']
            state = request.form['state']
            country = request.form['country']
            address = request.form['address']
            open_time = request.form['open_time']
            close_time = request.form['close_time']

            # Get the form values for table salon_services
            hair = request.form['hair']
            skin = request.form['skin']
            nail = request.form['nail']
            massage = request.form['massage']
            wax = request.form['wax']
            makeup = request.form['makeup']
            with engine.connect() as con:
                result = con.execute(text(f"select * from profile where email_id = '{username}' and password = '{password}' "))
                account = result.fetchone()
                con.commit()
                if account:
                    session['loggedin'] = True
                    session['id'] = account.id
                    session['username'] = account.username
                    return render_template('home_business.html', account = account)
            
            # Insert the values into table salon_contact & salon_services
            with engine.connect() as con:
                spot = con.execute(text(f"select spot_id from profile where email_id = '{username}' "))
                con.execute(text(f"insert into salon_contact (spot_id,phone,city,state,country,address,opening_time,closing_time) \
                                  values ('{spot}', '{phone}','{city}','{state}', '{country}', '{address}', '{open_time}', '{close_time}'\
                                      ) where spot_id = '{spot}'"))
                con.execute(text(f"insert into salon_services (spot_id,hair,skin,nails,massage,wax,makeup) \
                                 values ( '{spot}', '{hair}', '{skin}', '{nail}', '{massage}', '{wax}', '{makeup}' ) \
                                    where spot_id = '{spot}'"))
                con.commit()
        except Exception as e:
            print(e)
            return render_template('signin_business_account.html', e=e)
    return render_template('home_business.html')

@app.route('/home_admin', methods = ['get', 'post'])
def home_admin():
    return render_template('home_admin.html')

@app.route('/customer_display', methods= ['get','post'])
def customer_display():
    return render_template('customer_display.html')



# @app.route('/home_business', methods = ['get', 'post'])
# def home_business():
#     msg = ''
#     if request.method == 'post' and 'businessname' in request.form:
#         spot_it = request.form 




if __name__ == '__main__':
    app.run(port=8080, debug=True)
