from app import app
from flask import Flask, session, flash, redirect, render_template, request
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) 

from app.models.user_model import User

#default home screen route
@app.route('/')
def home():
    return render_template('access.html')

#route to handle registering a user
@app.route('/register/user', methods=['POST'])
def register_user():
    print(request.form)
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'confirm_password': request.form['confirm_password'],
    }
    # validate info
    if not User.validate_user(data):
        flash('registration unsuccessful')
        return redirect("/")
    #hash password
    data['password'] =  bcrypt.generate_password_hash(data['password'])
    # save user
    user_id = User.save_user(data)
    session['id'] = user_id
    # add user to session
    for key in data:
        session[f'{key}'] = data[f'{key}']
    print(session)
    # redirect to dashboard
    return redirect('/dashboard')

@app.route('/login/user', methods=['POST'])
def login_user():
    #search user by their email
    search = User.get_users_with_email(request.form['email'])
    user = search[0]
    print(f'USER is {search}')
    #validate email exists in the DB 
        #if false redirect back to ("/')
    if len(search) < 1 :
        flash('INVALID LOGIN CREDENTIALS', 'login')
        return redirect('/')
    #compare hash password input to the stored hash password
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('INVALID LOGIN CREDENTIALS', 'login')
        return redirect('/')
    #if match is true then add user to session and redirect to dashboard
    session['id']:user.id
    return redirect('/dashboard')

#route to the dashboard upon login or successful registration 
@app.route('/dashboard')
def dashboard():
    if not 'id' in session:
        return redirect('/')
    return render_template('dashboard.html')