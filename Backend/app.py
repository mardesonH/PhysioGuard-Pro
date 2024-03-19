from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv('DB_URL')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Definindo o modelo User
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

# Rota para retornar todos os usuários
@app.route("/users")
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
        user_list.append(user_data)
    return jsonify(user_list)

# Rota básica
@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
