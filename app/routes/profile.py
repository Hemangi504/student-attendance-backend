from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.main import app
from app.config.database import mysql

@app.route('/api/admin/profile', methods=['GET'])
@jwt_required()
def get_profile():

    email = get_jwt_identity()

    cursor = mysql.connection.cursor()
    cursor.execute(
        "SELECT username, email FROM admins WHERE email=%s",
        (email,)
    )

    admin = cursor.fetchone()
    cursor.close()

    if admin:
        return jsonify({
            "status": True,
            "username": admin[0],
            "email": admin[1]
        }), 200

    return jsonify({
        "status": False,
        "message": "Admin not found"
    }), 404