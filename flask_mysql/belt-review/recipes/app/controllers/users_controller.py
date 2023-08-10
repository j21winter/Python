from app import app
from flask import Flask, session, flash, redirect, render_template, request
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) 

from app.models.user_model import User
from app.models import recipe_model


#default home screen route
@app.route('/')
def home():
    return render_template('access.html')

#route to handle registering a user
@app.route('/register/user', methods=['POST'])
def register_user():
    # validate info
    if not User.validate_user(request.form):
        flash('registration unsuccessful')
        return redirect("/")
    # save user & add user to session
    session['id'] = User.save_user(
        {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': request.form['password']
            })
    # redirect to dashboard
    return redirect('/dashboard')

# route to handle login 
@app.route('/login/user', methods=['POST'])
def login_user():
    # search user by their email
    search = User.get_users_with_email(request.form['email'])
    # validate email exists in the DB 
        # if false redirect back to ("/')
    if len(search) < 1 :
        flash('INVALID LOGIN CREDENTIALS', 'login')
        return redirect('/')
    user = search[0]
    print(f'USER is {search}')
    # compare hash password input to the stored hash password
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('INVALID password CREDENTIALS', 'login')
        return redirect('/')
    # if match is true then add user to session and redirect to dashboard
    session['id'] = user.id
    return redirect('/dashboard')

#route to the dashboard upon login or successful registration 
@app.route('/dashboard')
def dashboard():
    if not 'id' in session:
        return redirect('/logout')
    user = User.get_one(session['id'])
    recipes = recipe_model.Recipe.get_all()
    return render_template('dashboard.html', user = user, recipes = recipes)

#route to log user out of the website and clear session
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')