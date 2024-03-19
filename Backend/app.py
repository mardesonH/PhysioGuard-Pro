from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

from models.models import User

load_dotenv()

DB_URL = os.getenv('DB_URL')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Rota para retornar todos os usuários
@app.route("/users")
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'team': user.team,
            'createdat': user.createdAt,
            'updatedat': user.updatedAt,
            'role': user.role 
        }
        user_list.append(user_data)
    return jsonify(user_list)

# Rota básica
@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
