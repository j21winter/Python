from app import app
from flask import Flask, session, flash, redirect, render_template, request
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) 
from app.models import user_model

@app.route('/')
def home():
    return render_template('index.html')

#? Processing of the registration form!
@app.route('/register/user', methods=['POST'])
def register_user():
    user = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'conf_password': request.form['conf_password']
        }
    if not user_model.User.validate_registration(user):
        flash('**Registration failed!**', 'registration')
        return redirect('/')
    hashed_password = bcrypt.generate_password_hash(user['password'])
    print(hashed_password)
    user['password'] = hashed_password
    user_id = user_model.User.save(user)
    session['first_name']= request.form['first_name']
    session['last_name']= request.form['last_name']
    session['email']= request.form['email']
    session['id']= user_id
    print(session)
    return redirect('/success')

@app.route('/login/user', methods=['POST'])
def login():
    user = user_model.User.get_emails(request.form['email'])[0]
    if not user:
        flash('invalid login credentials', 'login_error')
        return redirect ('/')
    print(user.email, user.password)
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('invalid login credentials', 'login_error')
        return redirect ('/')
    session['id'] = user.id
    return redirect('/success')

@app.route('/success')
def success():
    if not 'id' in session:
        return redirect('/')
    return render_template('success.html')

@app.route('/logout')
def logout():
    session.clear()
    print(session)
    return redirect('/')