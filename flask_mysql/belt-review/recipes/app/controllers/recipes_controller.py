from app import app
from flask import Flask, session, flash, redirect, render_template, request

from app.models.recipe_model import Recipe
from app.models import user_model

@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html')


@app.route('/save_recipe', methods=['POST'])
def save_recipe():
    #validate the form 
    if not Recipe.validate_recipe(request.form):
        flash('Adding recipe failed! Please try again', 'add_recipe')
        return redirect('/add_recipe')
    
    #call on save_recipe
    recipe_id = Recipe.save_recipe({
        'name': request.form['name'], 
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'under_30_mins': request.form['under_30_mins'], 
        'date_cooked': request.form['date_cooked'], 
        'user_id': request.form['user_id']
    })
    return redirect('/dashboard')

@app.route('/edit/recipe/<int:id>')
def display_edit_recipe(id):
    print(f'ID = {id}')
    recipe = Recipe.get_one(id)
    return render_template('edit_recipe.html', recipe = recipe)

# !!!!!!!!!!!!!!

@app.route('/update_recipe', methods=['POST'])
def edit_recipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        flash('Updating recipe failed! Please try again', 'add_recipe')
        return redirect(f'/edit/recipe/{request.form["recipe_id"]}')
    Recipe.update_recipe(request.form)
    return redirect('/dashboard')

