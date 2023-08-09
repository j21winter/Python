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

#! next we will be looking to create the edit recipe and the show recipe page