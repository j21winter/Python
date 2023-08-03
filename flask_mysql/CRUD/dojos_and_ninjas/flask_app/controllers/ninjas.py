from flask_app import app
from flask import Flask, render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


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

@app.route('/add_ninja')
def add_ninja_display():
    dojos = Dojo.get_all_dojos()
    return render_template('ninjas.html', dojos = dojos)

@app.route('/delete/<int:id>')
def delete_ninja(id):
    dojo_id = Ninja.dojo_id_by_ninja(id)
    print(dojo_id[0])
    Ninja.delete_ninja(id)
    return redirect(f'/dojo/{dojo_id[0]["dojo_id"]}')

@app.route('/update/<int:id>')
def display_update_ninja_form(id):
    ninja = Ninja.get_ninja_by_id(id)
    print(ninja)
    dojos = Dojo.get_all_dojos()
    print(f'dojos = {dojos}')
    return render_template('/update_ninja.html', ninja = ninja, dojos = dojos)

@app.route('/updating', methods=['POST'])
def update_ninja_process():
    data = {
        'id': request.form['id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    Ninja.edit_ninja(data)
    return redirect(f'/dojo/{request.form["id"]}')