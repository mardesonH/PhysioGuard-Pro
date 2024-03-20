from flask import Blueprint, jsonify, request
from models import Athlete, User
from app import db, jwt
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
import jwt

registerAthlete_blueprint = Blueprint('registerAthlete', __name__)

@registerAthlete_blueprint.route('/registerAthlete', methods=['POST'])
@jwt_required()
def create_athlete():
    try:
        token = request.headers.get('Authorization').split(" ")[1]
        print("Token recebido:", token)

        decoded_token = jwt.decode(token, 'mardeson' ,algorithms=["HS256"]) 
        print("Token decodificado:", decoded_token)

        email = decoded_token['sub']
        print("Email do usuário:", email)

        user = User.query.filter_by(email=email).first()

        if user:
            user_id = user.id
            team = user.team
        else:
            user_id = 1
            team = 'Time Padrão'

        # Verifica se a requisição contém o JSON esperado
        if not request.is_json:
            return jsonify({'error': 'A requisição deve ser JSON'}), 400

        data = request.json
        name = data.get('name')
        birthDate = data.get('birthDate')
        number = data.get('number')
        position = data.get('position')

        if not name or not birthDate or not number or not position:
            return jsonify({'error': 'Campos incompletos!'}), 400

        existing_athlete = Athlete.query.filter_by(name=name).first()
        if existing_athlete:
            return jsonify({'error': 'O atleta já está cadastrado!'}), 400

        new_athlete = Athlete(
            name=name,
            birthDate=datetime.strptime(birthDate, '%d/%m/%Y'),
            number=number,
            position=position,
            team=team,
            registeredBy=user_id,
            updatedBy=user_id
        )
        
        db.session.add(new_athlete)
        db.session.commit()

        return jsonify({'message': 'Atleta cadastrado com sucesso!'}), 201
    except Exception as e:
        print("Erro durante a criação do atleta:", e)
        return jsonify({'error': 'Erro durante a criação do atleta'}), 500
