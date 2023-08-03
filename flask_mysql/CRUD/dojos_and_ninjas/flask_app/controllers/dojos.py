from flask_app import app
from flask import Flask, render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return redirect('/dojo')

@app.route('/dojo')
def render_dojos():
    dojos = Dojo.get_all_dojos()
    return render_template('dojo.html', dojos = dojos)

@app.route('/save_dojo', methods=['POST'])
def save_dojo():
    Dojo.save_dojo(request.form['new_dojo_name'])
    return redirect('/')

@app.route('/dojo/<int:id>')
def render_dojo_by_id(id):
    dojo = Dojo.get_dojo_with_ninjas(id)
    print(dojo)
    return render_template('show_dojo.html', dojo = dojo)



