import re
from app import app
from app.config.mysqlconnection import connectToMySQL
from app.models import ride_model
from flask import Flask, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
PASSWORD_REGEX = re.compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$")

class User:
    db = 'rideshare'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.driving_list = []
        self.riding_list = []

    #add users to DB
    @classmethod
    def create_user(cls, data):
        data['password'] =  bcrypt.generate_password_hash(data['password'])
        
        query = '''
                INSERT INTO users (first_name, last_name, email, password)
                VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s);
                '''
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def get_user_with_email(cls,email):
        print('GETTING USER WITH EMAIL')
        query = '''
                SELECT * FROM users
                WHERE email = %(email)s;'''
        results = connectToMySQL(cls.db).query_db(query, {'email': email})
        if len(results) < 1:
            return False
        else:
            print(f'GETTING USERS sending back {results[0]}')
            return cls(results[0])
        
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
        if User.get_user_with_email(data['email']):
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

