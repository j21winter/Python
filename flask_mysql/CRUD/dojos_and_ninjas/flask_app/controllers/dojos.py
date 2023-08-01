from flask_app import app
from flask import Flask, render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def render_dojos():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos = dojos)

@app.route('/save_dojo', methods=['POST'])
def save_dojo():
    Dojo.save_dojo(request.form['new_dojo_name'])
    return redirect('/')

@app.route('/dojo/<int:id>')
def render_dojo_by_id(id):
    dojo = Dojo.get_one(id)
    print(dojo)
    ninjas = Ninja.get_ninjas_by_dojo_id(id)
    return render_template('show_dojo.html', dojo = dojo[0], ninjas = ninjas )

@app.route('/add_ninja')
def add_ninja_display():
    dojos = Dojo.get_all()
    return render_template('ninjas.html', dojos = dojos)

@app.route('/save_ninja',methods=['POST'])
def save_ninja():
    print(request.form['dojo'])
    data = {
        'dojo': request.form['dojo'], 
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    print(data)
    Ninja.save_ninja(data)
    return redirect (f'/dojo/{request.form["dojo"]}')