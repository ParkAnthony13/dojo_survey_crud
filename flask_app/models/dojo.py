from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# from flask_app.models.ninja import ### other models ###


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(Dojo(dojo))
        return dojos
    

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id=%(id)s"
        results = connectToMySQL('dojo_survey_schema').query_db(query,data)
        return results[0]


    @classmethod
    def insert(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES ( %(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
        return connectToMySQL('dojo_survey_schema').query_db(query, data)



    @staticmethod
    def validate_user(user):
        is_valid = True # the keys must match the request.form keys or NAME in the HTML
        if len(user['full_name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(user['location']) < 3:
            flash("location must be at least 3 characters.")
            is_valid = False
        if len(user['language']) < 3:
            flash("language must be at least 3 characters.")
            is_valid = False
        # else:       this statement to make sure that input is a nubmer
        #     if not post_data['age'].isnumeric():
        #         flash("Age must be a number")
        #         is valid = False
        return is_valid