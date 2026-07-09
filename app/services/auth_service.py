from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.config.database import mysql


class AuthService:

    @staticmethod
    def signup(username, email, password):
        cursor = mysql.connection.cursor()

        cursor.execute(
            "SELECT * FROM admins WHERE username=%s OR email=%s",
            (username, email)
        )

        admin = cursor.fetchone()

        if admin:
            cursor.close()
            return {"message": "Admin already exists"}

        hashed_password = generate_password_hash(password)

        cursor.execute(
            "INSERT INTO admins(username,email,password) VALUES(%s,%s,%s)",
            (username, email, hashed_password)
        )

        mysql.connection.commit()
        cursor.close()

        return {"message": "Signup successful"}

    @staticmethod
    def login(username, password):
        cursor = mysql.connection.cursor()

        cursor.execute(
            "SELECT * FROM admins WHERE username=%s",
            (username,)
        )

        admin = cursor.fetchone()
        cursor.close()

        if not admin:
            return {"message": "Invalid username"}

        if check_password_hash(admin[3], password):
            token = create_access_token(identity=admin[1])

            return {
                "message": "Login successful",
                "token": token
            }

        return {"message": "Invalid password"}

    @staticmethod
    def forgot_password(username, new_password):
        cursor = mysql.connection.cursor()

        hashed_password = generate_password_hash(new_password)

        cursor.execute(
            "UPDATE admins SET password=%s WHERE username=%s",
            (hashed_password, username)
        )

        mysql.connection.commit()
        cursor.close()

        return {"message": "Password updated"}

    @staticmethod
    def logout():
        return {"message": "Logout successful"}
    