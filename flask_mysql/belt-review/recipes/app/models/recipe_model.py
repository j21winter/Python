from app.config.mysqlconnection import connectToMySQL
from flask import Flask, flash
from app.models import user_model

class Recipe:
    db = 'recipes'
    
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30_mins = data['under_30_mins']
        self.date_cooked = data['date_cooked']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
    
    #I do not like the way that I am finding the name. There has got to be a way to make this work without the wierd for loop at the end appending the name to the recipe object
    @classmethod
    def get_all(cls):
        print(f'GETTING recipes')
        query = '''
                SELECT * FROM recipes
                LEFT JOIN users 
                ON recipes.user_id = users.id;
                '''
        results = connectToMySQL(cls.db).query_db(query)
        recipes = []
        for row in results:
            recipe = (cls(row))
            recipe.user_name = user_model.User.get_one(recipe.user_id).first_name
            recipes.append(recipe)
        return recipes
    
    @classmethod
    def save_recipe(cls, data):
        print('SAVING RECIPE')
        query = '''
                INSERT INTO recipes (name, description, instructions, under_30_mins, date_cooked, user_id)
                VALUES(%(name)s,%(description)s,%(instructions)s,%(under_30_mins)s, %(date_cooked)s, %(user_id)s);
                '''
        return connectToMySQL(cls.db).query_db(query, data)
    
    #validate recipe form information
    @staticmethod
    def validate_recipe(data):
        # Set is_valid to true as default
        is_valid = True
        print(data)
        for key in data:
            if len(data[f"{key}"])< 1:
                    flash(f'{key} field must be filled', 'add_recipe')
                    is_valid = False
        return is_valid

# add folder to workspace
# debugger
# click debugger
# drop down 
# config for the file you are working on 
# run with python 
# run with flask framework
#     change debug flask from app.py to server.py
# set the environment for the debugger


