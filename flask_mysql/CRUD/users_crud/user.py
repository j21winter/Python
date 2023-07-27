from mysqlconnection import connectToMySQL

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
                    SET first_name = %(first_name)s,last_name = %(last_name)s, email = %(email)s
                    WHERE users.id = %(id)s;'''

        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete_user(cls, user_id):
        query = 'DELETE FROM users WHERE users.id = %(id)s'
        data = {'id':user_id}
        return connectToMySQL(cls.DB).query_db(query, data)
