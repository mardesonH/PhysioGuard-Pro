from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv('DB_URL')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importando os blueprints
from routes.registerUser import registerUser_blueprint
from routes.users import users_blueprint

# Registrando os blueprints
app.register_blueprint(registerUser_blueprint)
app.register_blueprint(users_blueprint)

if __name__ == '__main__':
    app.run()
