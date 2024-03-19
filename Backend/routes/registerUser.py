from flask import Blueprint, jsonify, request
from models import User
from app import db

registerUser_blueprint = Blueprint('registerUser', __name__)

@registerUser_blueprint.route('/registerUser', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    team = data.get('team')
    role = data.get('role')

    if not username or not email or not password or not team or not role:
        return jsonify({'error': 'Campos incompletos!'}), 400

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'error': 'O usuário já existe!'}), 400

    if User.query.filter_by(team=team).count() >= 5:
        return jsonify({'error': 'O time já atingiu o máximo de usuários!'}), 400

    new_user = User(username=username, email=email, team=team, role=role)
    new_user.set_password(password)
    
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Usuário criado com sucesso!'}), 201
