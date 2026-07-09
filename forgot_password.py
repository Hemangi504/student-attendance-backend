from flask import request, jsonify
from app.main import app
from app.config.database import mysql

@app.route('/api/admin/forgot_password', methods=['POST'])
def forgot_password():

    data = request.get_json()

    email = data.get('email')
    new_password = data.get('new_password')

    cursor = mysql.connection.cursor()

    cursor.execute("SELECT * FROM admins WHERE email=%s", (email,))
    user = cursor.fetchone()

    if not user:
        cursor.close()
        return jsonify({
            "status": False,
            "message": "Email not found"
        }), 404

    cursor.execute(
        "UPDATE admins SET password=%s WHERE email=%s",
        (new_password, email)
    )

    mysql.connection.commit()
    cursor.close()

    return jsonify({
        "status": True,
        "message": "Password Updated Successfully"
    }), 200