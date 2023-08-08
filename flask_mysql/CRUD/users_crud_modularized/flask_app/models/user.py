import re
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    DB = 'users_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def get_email(cls, email):
        print('\n GETTING EMAIL \n')
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL('users_schema').query_db(query, {'email': email})
        emails = []
        for email in results:
            emails.append(email['email'])
        print(emails)
        return emails
    
    @classmethod
    def get_one_by_id(cls,user_id):
        query = 'SELECT * FROM users WHERE users.id = %(id)s;'
        data = {'id': user_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    
    @classmethod
    def save(cls, data):
        query = """INSERT INTO users(first_name, last_name, email, created_at, updated_at) 
                    VALUES (%(first_name)s,%(last_name)s,%(email)s, NOW(),NOW());"""
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def update_user(cls,data):
        query = '''
                    UPDATE users
                    SET first_name = %(first_name)s,last_name = %(last_name)s, email = %(email)s, updated_at = NOW()
                    WHERE users.id = %(id)s;'''
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete_user(cls, user_id):
        query = 'DELETE FROM users WHERE users.id = %(id)s'
        data = {'id':user_id}
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @staticmethod
    def validate_user(user):
        is_valid = True
        print('\n VALIDATING FORM... \n')
        print(f'\n user is: {user} \n')

        # first name validation
        if len(user['first_name']) < 3:
            if len(user['first_name']) < 1:
                flash('First Name required!', 'first_name')
                is_valid = False
            else:
                flash('First name must be at least 3 characters', 'first_name')
                is_valid = False
        
        # Last name validation
        if len(user['last_name']) < 3:
            if len(user['last_name']) < 1:
                flash('Last Name required!', 'last_name')
                is_valid = False
            else:
                flash('Last name must be at least 3 characters', 'last_name')
                is_valid = False
        
        # Email name validation
        email = User.get_email(user['email'])
        if len(user['email']) < 1:
            flash('Email required!', 'email')
            is_valid = False
        elif not EMAIL_REGEX.match(user['email']):
            flash('Invalid email format', 'email')
            is_valid = False
        elif email:
            flash('email address already in use, please provide a unique email', 'email')
            is_valid = False
        return is_valid
