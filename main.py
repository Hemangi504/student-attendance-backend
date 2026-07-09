from flask import Flask
from app.config.database import mysql,jwt

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root123'
app.config['MYSQL_DB'] = 'studentdb'

app.config['JWT_SECRET_KEY'] = 'mysecretkey'

mysql.init_app(app)
jwt.init_app(app)

from app.routes.login import *
from app.routes.signup import *
from app.routes.forgot_password import *
from app.routes.logout import *
from app.routes.profile import*


if __name__ == "__main__":
    app.run(debug=True, port=3000)