from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)  # Adicionando campo senha
    team = db.Column(db.String(64), nullable=False)  # Adicionando campo team
    createdAt = db.Column(db.DateTime, nullable=False, server_default=db.func.now())  # Adicionando campo createdAt
    updatedAt = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())  # Adicionando campo updatedAt
    role = db.Column(db.Integer(), nullable=False)  # Adicionando campo role
