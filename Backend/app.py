from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
import os

load_dotenv()

DB_URL = os.getenv('DB_URL')

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "mardeson" 
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
jwt = JWTManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)



# Importando os blueprints
from routes.registerUser import registerUser_blueprint
from routes.users import users_blueprint
from routes.login import login_blueprint

# Registrando os blueprints
app.register_blueprint(registerUser_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(login_blueprint)


if __name__ == '__main__':
    app.run()
