from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, DateTime, func
import bcrypt
from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    team = db.Column(db.String(), nullable=False)
    role = db.Column(db.String(), nullable=False)
    createdAt = Column(DateTime, nullable=False, default=func.now())
    updatedAt = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

    def set_password(self, password):
        salt = bcrypt.gensalt()
        if isinstance(password, str):
            password = password.encode('utf-8')
        self.password = bcrypt.hashpw(password, salt).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))


class Athlete(db.Model):
    __tablename__ = 'athletes'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    number = Column(Integer, nullable=False)
    birthDate = Column(Date, nullable=False)
    position = Column(String(64), nullable=False)
    team = Column(String(64), nullable=False)
    createdAt = Column(DateTime, nullable=False, default=func.now())
    updatedAt = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
    registeredBy = Column(Integer, nullable=False)
    updatedBy = Column(String(64), nullable=False)

    def __repr__(self):
        return f"<Athlete(name='{self.name}', number='{self.number}', position='{self.position}')>"
