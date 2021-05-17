# dojo.py
from flask_app.config.mysqlconnection import connectToMySQL

from .ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # we need to build a list of ninjas related to the dojo (many ninjas to one dojo)  
        self.ninjas = []

    # get all dojos and return them in a list of objects 
    # cls refers to the class - standard naming convention for a class method
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"

        dojos_from_db = connectToMySQL("dojos_and_ninjas").query_db(query)
        
        dojos = [] # to hold the list of dojo onbjects

        for dojo in dojos_from_db:
            # add dojo objects to the dojos list
            dojos.append(cls(dojo))

        #return the list of dojos    
        return dojos

    # gets one user and returns the user with a matching user id
    @classmethod
    def get_dojo_with_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        
        results = connectToMySQL("dojos_and_ninjas").query_db(query,data)
        
        # creating an instance of a dojo with the raw data coming back
        # use results[0] because the data comes back as a list.
        my_dojo = cls(results[0])

        # iterate over the list and add artist objects into the group attribute of artists
        for row in results:
            data={
                "id": row['ninjas.id'],
                "dojo_id": row['id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "age": row['age'],
                "created_at": row['ninjas.created_at'],
                "updated_at": row['ninjas.updated_at']
            }

            # create a Ninja object & add it to the list of ninjas assoicated with the dojo
            my_dojo.ninjas.append(Ninja(data))
        
        return my_dojo


    # create a new dojo and insert the dojo into the daatabase
    @classmethod
    def add_dojo(cls,new_dojo):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        
        dojo_id = connectToMySQL("dojos_and_ninjas").query_db(query,new_dojo)

        return dojo_id