from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
class Dojo:
    DB = 'dojos_and_ninjas_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def get_all_dojos(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def get_one_dojo(cls, id):
        query = 'SELECT * FROM dojos WHERE id = %(id)s'
        result = connectToMySQL(cls.DB).query_db(query,{'id' : id})
        return cls(result)
    
    @classmethod
    def save_dojo(cls, name):
        query = 'INSERT INTO dojos(name) VALUES(%(name)s);'
        result = connectToMySQL(cls.DB).query_db(query, {'name': name})
        return result
    

    @classmethod
    def get_dojo_with_ninjas(cls, dojo_id):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(dojo_id)s;'
        result = connectToMySQL(cls.DB).query_db(query, {'dojo_id': dojo_id})
        print(result)
        dojo = cls(result[0])
        for row in result:
            ninja_data = {
            'id' : row['ninjas.id'],
            'first_name':row['first_name'],
            'last_name':row['last_name'],
            'age':row['age'],
            'created_at':row['ninjas.created_at'],
            'updated_at':row['ninjas.updated_at'],
            'dojo_id':row['dojo_id']
            }
        dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo

