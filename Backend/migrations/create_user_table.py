from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/physioguardpro'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Definição do modelo User
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


def create_tables():
    db.create_all()

def drop_tables():
    db.drop_all()
