from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']


# Create a ninja
    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at) VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW());"
        return connectToMySQL('dojos_and_ninja_ii').query_db(query, data)
    

# Read ninja information

    @classmethod
    def get_ninja_info(cls, ninja_id):
        query = "SELECT * FROM ninjas WHERE id = %(ninja_id)s;"
        data = {
            "ninja_id": ninja_id
        }
        results = connectToMySQL('dojos_and_ninja_ii').query_db(query, data)
        ninja = results[0]
        return ninja

# Update / Edit a ninja
    @classmethod
    def edit_one_ninja(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninja_ii').query_db(query, data)

# Delete a ninja
    @classmethod
    def delete_user_by_id(cls, ninja_id):
        query = "DELETE FROM ninjas WHERE id = %(ninja_id)s;"
        data = {
            "ninja_id": ninja_id
        }
        return connectToMySQL('dojos_and_ninja_ii').query_db(query, data)