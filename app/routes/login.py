from flask import request, jsonify
from flask_jwt_extended import create_access_token
from app.main import app
from app.config.database import mysql

@app.route('/api/admin/login', methods=['POST'])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    cursor = mysql.connection.cursor()

    cursor.execute(
        "SELECT * FROM admins WHERE email=%s AND password=%s",
        (email, password)
    )

    user = cursor.fetchone()
    cursor.close()

    if user:
        token = create_access_token(identity=email)

        return jsonify({
            "status": True,
            "message": "Login Successful",
            "token": token
        }), 200

    return jsonify({
        "status": False,
        "message": "Invalid Email or Password"
    }), 401

