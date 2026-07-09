from flask import request, jsonify
from app.main import app
from app.config.database import mysql

@app.route('/api/admin/signup', methods=['POST'])
def signup():

    data = request.get_json()

    print(type(data))
    print(data)
    
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    cursor = mysql.connection.cursor()

    cursor.execute("SELECT * FROM admins WHERE email=%s", (email,))
    user = cursor.fetchone()

    if user:
        cursor.close()
        return jsonify({
            "status": False,
            "message": "Email already exists"
        }), 409

    cursor.execute(
        "INSERT INTO admins(username, email, password) VALUES(%s, %s, %s)",
        (username, email, password)
    )

    mysql.connection.commit()
    cursor.close()

    return jsonify({
        "status": True,
        "message": "Signup Successful"
    }), 201
