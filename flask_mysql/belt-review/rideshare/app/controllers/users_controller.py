from app import app
from flask import Flask, session, flash, redirect, render_template, request
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) 

from app.models.user_model import User

#default home screen route
@app.route('/')
def home():
    return render_template('user_login.html')

#route to handle registering a user
@app.route('/user/create', methods=['POST'])
def register_user():

    # validate info
    if not User.validate_user(request.form):
        flash('registration unsuccessful')
        return redirect("/")
    
    # save user & add user to session
    session['first_name'] = request.form['first_name']
    session['id'] = User.create_user({
                                        'first_name': request.form['first_name'],
                                        'last_name': request.form['last_name'],
                                        'email': request.form['email'],
                                        'password': request.form['password']
                                        })
    
    # redirect to dashboard
    return redirect('/user/dashboard')

# route to handle login 
@app.route('/user/login', methods=['POST'])
def login_user():
    # search user by their email
    user = User.get_user_with_email(request.form['email'])

    # validate email exists in the DB 
        # if false redirect back to ("/')
    if not user:
        flash('INVALID LOGIN CREDENTIALS', 'login')
        return redirect('/')
    
    # compare hash password input to the stored hash password
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('INVALID password CREDENTIALS', 'login')
        return redirect('/')
    
    # if match is true then add user to session and redirect to dashboard
    session['id'] = user.id
    session['first_name'] = user.first_name

    return redirect('/user/dashboard')

#route to log user out of the website and clear session
@app.route('/user/logout')
def logout():

    session.clear()

    return redirect('/')