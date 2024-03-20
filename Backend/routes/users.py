from flask import Blueprint, jsonify
from models import User
from app import db

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route("/users")
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'team': user.team,
            'createdAt': user.createdAt,
            'updatedAt': user.updatedAt,
            'role': user.role 
        }
        user_list.append(user_data)
    return jsonify(user_list)
