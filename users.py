from flask.templating import render_template
from mysqlconnection import connectToMySQL



class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('first_flask').query_db(query)
        users = []

        for user in results:
            # user_data = {
            #     "id" : user["user.id"],
            #     "first_name" : user["user.first_name"],
            #     "last_name" : user["user.last_name"],
            #     "email" : user["user.email"],
            #     "created_at" : user ["user.created_at"],
            #     "updated_at" : user["user.updated_at"]
            # }
            # users.append(user.User(user_data))
            users.append(cls(user))
        return users


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE users.id = %(id)s"
        results = connectToMySQL('first_flask').query_db(query, data)
        return cls (results[0])

        # for user in results:
        #     user_data = {
        #         "id" : user["user.id"],
        #         "first_name" : user["user.first_name"],
        #         "last_name" : user["user.last_name"],
        #         "email" : user["user.email"],
        #         "created_at" : user ["user.created_at"],
        #         "updated_at" : user["user.updated_at"]
        #     }
        # return user_data.id
        print(results)



    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL('first_flask').query_db(query, data)

    @classmethod
    def delete_user(cls, data):
        query = "DELETE first_flask.users FROM users WHERE id = %(id)s;"
        connectToMySQL('first_flask').query_db(query, data)
        return

    @classmethod
    def update_user(cls, data):
        query = "UPDATE first_flask.users SET first_name = %(first_name)s,  last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE users.id = %(id)s"
        results = connectToMySQL('first_flask').query_db(query, data)
        return results

