from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Doctor(db.Model):
    
    __tablename__ = 'doctors_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    specialty = db.Column(db.String)


class Patient(db.Model):
    
    __tablename__ = 'patients_table'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


class Appointment(db.Model):
    
    __tablename__ = 'appointments_table'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)