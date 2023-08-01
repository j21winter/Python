from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    DB = 'dojos_and_ninjas_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    
    @classmethod
    def get_ninjas_by_dojo_id(cls, dojo_id):
        query = 'SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;'
        results = connectToMySQL(cls.DB).query_db(query, {'dojo_id': dojo_id})
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
    
    @classmethod
    def save_ninja(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo)s);'
        return connectToMySQL(cls.DB).query_db(query, data)

