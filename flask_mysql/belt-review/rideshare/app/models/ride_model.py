from app.config.mysqlconnection import connectToMySQL
from flask import Flask, flash
from app.models import user_model

class Ride:

    db = 'rideshare'
    
    def __init__(self, data):
        self.id = data['id']
        self.destination = data['destination']
        self.pick_up_location = data['pick_up_location']
        self.details = data['details']
        self.date = data['date']
        self.rider_id = data['rider_id']
        self.driver_id = data['driver_id']

    @classmethod
    def create_ride(cls, data):
        print('creating ride')
        query = '''
                INSERT INTO rides (destination, pick_up_location, date, rider_id)
                VALUES(%(destination)s,%(pick_up_location)s,%(date)s,%(rider_id)s);
                '''
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_ride(data):
        is_valid = True

        for key in data:
            if len(data[f"{key}"])< 1:
                    flash(f'{key} field must be filled', 'add_ride')
                    is_valid = False
        
        return is_valid