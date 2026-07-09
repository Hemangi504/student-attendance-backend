from config import mysql
from flask import jsonify

class Admin:

 def __init__(self, username, email, password):
    self.username = username
    self.email = email
    self.password = password

 def to_dict(self):
     return {
         "username": self.username,
            "email": self.email
        }
 
 @staticmethod
 def get_by_username(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM admins WHERE username = %s", (username,))
    admin = cursor.fetchone()
    cursor.close()
    return admin
 
 

 