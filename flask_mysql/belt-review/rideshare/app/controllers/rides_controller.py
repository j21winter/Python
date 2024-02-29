from app import app
from flask import Flask, session, flash, redirect, render_template, request

from app.models.ride_model import Ride

@app.route('/ride/form')
def ride_form():
    if not 'id' in session:
        return redirect('/')
    return render_template('request_ride.html')

@app.route('/ride/create', methods=['POST'])
def create_ride():
    if not 'id' in session:
        return redirect('/')
    
    if not Ride.validate_ride(request.form):
        flash('Adding ride failed! Please try again', 'add_ride')
        return redirect('/ride/form')
    
    Ride.create_ride(request.form)

    return redirect('/user/dashboard')