import re
from app.config.mysqlconnection import connectToMySQL
from flask import Flask, flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
PASSWORD_REGEX = re.compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$")

class User:
    DB = 'users_login'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def save(cls, data):
        query = '''
                INSERT INTO users (first_name, last_name, email, password)
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)'''
        new_user_id = connectToMySQL(cls.DB).query_db(query, data)
        return new_user_id
    
    @classmethod
    def get_emails(cls, email):
        print('\n GETTING EMAIL \n')
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL(cls.DB).query_db(query, {'email': email})
        print(f'results = {results}')
        users = []
        for user in results:
            users.append(cls(user))
        print(f'get email response users list = {users}')
        return users
    
    @staticmethod
    def validate_registration(user):
        print('\n VALIDATING \n')
        is_valid = True

        # First name validation
        if len(user['first_name']) < 3:
            
            if len(user['first_name']) < 1:
                flash('First Name required!', 'registration')
                is_valid = False
            
            else:
                flash('First name must be at least 3 characters', 'registration')
                is_valid = False
        
        # Last name validation
        if len(user['last_name']) < 3:
        
            if len(user['last_name']) < 1:
                flash('Last Name required!', 'registration')
                is_valid = False
            
            else:
                flash('Last name must be at least 3 characters', 'registration')
                is_valid = False
        
        # Email validation
        print('\n VALIDATING EMAIL LENGTH\n')
        if len(user['email']) < 1:
            
            flash('Email required!', 'registration')
            is_valid = False
        
        print('\n VALIDATING EMAIL FORMAT\n')
        if not EMAIL_REGEX.match(user['email']):
            
            flash('Invalid email format', 'registration')
            print('\n EMAIL FORMAT FAILED\n')
            is_valid = False
        
        if len(User.get_emails(user['email']))>0:
            flash('email address already in use, please provide a unique email', 'registration')
            is_valid = False
            print('\n EMAIL not unique\n')
            
        # Password validation
        print('\n VALIDATING PASSWORD\n')
        
        if len(user['password']) < 8:
            if len(user['password']) < 1:
                flash('Password required!', 'registration')
                print('\n PASSWORD LENGTH FAILED\n')
                is_valid = False
            
            else:
                flash('Password must be at least 8 characters', 'registration')
                print('\n PASSWORD LENGTH FAILED\n')
                is_valid = False
        
        if not PASSWORD_REGEX.match(user['password']):
            flash('Invalid password format','registration')
            print('\n PASSWORD FORMAT FAILED\n')
            is_valid = False
        
        if user['password'] != user['conf_password']:
            flash('Passwords do not match', 'registration')
            print('\n PASSWORD MATCH FAILED\n')
            is_valid = False
        
        print(f'is_valid = {is_valid}')
        return is_valid

