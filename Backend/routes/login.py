from flask import jsonify, request, Blueprint
from flask_jwt_extended import create_access_token
from models import User
from app import app, jwt

login_blueprint = Blueprint('login', __name__)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid email or password"}), 401

    # Se as credenciais estiverem corretas, gerar um token JWT com expiração de 24 horas
    access_token = create_access_token(identity=email, expires_delta=False)

    return jsonify({"access_token": access_token}), 200
