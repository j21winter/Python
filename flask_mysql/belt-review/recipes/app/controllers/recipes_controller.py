from app import app
from flask import Flask, session, flash, redirect, render_template, request

from app.models.recipe_model import Recipe
from app.models import user_model

@app.route('/add_recipe')
def add_recipe():
    if not 'id' in session:
        return redirect('/')
    
    return render_template('add_recipe.html')



@app.route('/save_recipe', methods=['POST'])
def save_recipe():
    if not 'id' in session:
        return redirect('/')
    
    #validate the form 
    if not Recipe.validate_recipe(request.form):
        flash('Adding recipe failed! Please try again', 'add_recipe')
        return redirect('/add_recipe')
    
    #call on save_recipe
    Recipe.save_recipe(request.form)

    return redirect('/dashboard')



@app.route('/edit/recipe/<int:id>')
def display_edit_recipe(id):

    if not 'id' in session:
        return redirect('/')
    
    recipe = Recipe.get_one(id)

    if recipe.user_id != session['id']:
        return redirect('/logout')
    
    return render_template('edit_recipe.html', recipe =  recipe)



@app.route('/update_recipe', methods=['POST'])
def update_recipe():
    if not 'id' in session:
        return redirect('/')
    
    if not Recipe.validate_recipe(request.form):
        flash('Updating recipe failed! Please try again', 'add_recipe')
        return redirect(f'/edit/recipe/{request.form["recipe_id"]}')
    
    Recipe.update_recipe(request.form)

    return redirect('/dashboard')



@app.route('/show/recipe/<int:id>')
def show_recipe(id):
    if not 'id' in session:
        return redirect('/')
    
    return render_template('show_recipe.html', recipe =  Recipe.get_one(id))



@app.route('/delete/recipe/<int:id>')
def delete_recipe(id):
    if not 'id' in session:
        return redirect('/')
    
    Recipe.delete_recipe(id)

    return redirect('/dashboard')