import re
from app.config.mysqlconnection import connectToMySQL
from flask import Flask, flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
PASSWORD_REGEX = re.compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$")

class User:
    db = 'recipes'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []

    #add users to DB
    @classmethod
    def save_user(cls, data):
        print('SAVING USER')
        query = '''
                INSERT INTO users (first_name, last_name, email, password)
                VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s);
                '''
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    #find users with email
    @classmethod
    def get_users_with_email(cls,email):
        print('GETTING USERS WITH EMAIL')
        query = '''
                SELECT * FROM users
                WHERE email = %(email)s;'''
        results = connectToMySQL(cls.db).query_db(query, {'email': email})
        users_list = []
        for user in results:
            users_list.append(cls(user))
        print(f'GETTING USERS sending back {users_list}')
        return users_list
    
    #validate registration form information
    @staticmethod
    def validate_user(data):
        # Set is_valid to true as default
        is_valid = True

        #validate first name
        #length
        print('VALIDATING')
        if len(data['first_name'])<3:
            if len(data['first_name'])<1:
                flash('First name field must be filled', 'registration')
                is_valid = False
            else:
                flash('First name field must be more than 3 characters', 'registration')
                is_valid = False
        
        #validate last name
        #length
        if len(data['last_name'])<3:
            if len(data['last_name'])<1:
                flash('Last name field must be filled', 'registration')
                is_valid = False
            else:
                flash('Last name field must be more than 3 characters', 'registration')
                is_valid = False
        
        #validate email
        #length
        if len(data['email'])<1:
            flash('email field must be filled', 'registration')
            is_valid = False
        
        #format
        if not EMAIL_REGEX.match(data['email']):
            flash('Invalid email format', 'registration')
            print('\n EMAIL FORMAT FAILED\n')
            is_valid = False
        
        #unique
        if len(User.get_users_with_email(data['email'])) > 0:
            flash('Email not unique, please provide another', 'registration')
            is_valid = False

        #validate password
        #length
        if len(data['password'])<3:
            if len(data['password'])<1:
                flash('Password name field must be filled', 'registration')
                is_valid = False
            else:
                flash('Password name field must be more than 8 characters', 'registration')
                is_valid = False
        #FORMAT
        if not PASSWORD_REGEX.match(data['password']):
            flash('Invalid Password format', 'registration')
        #password match
        if data['password'] != data['confirm_password']:
            flash('Passwords do not match', 'registration')
            is_valid = False
        
        print(is_valid)
        return is_valid

