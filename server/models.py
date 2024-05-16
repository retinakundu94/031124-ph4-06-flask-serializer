from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Doctor(db.Model, SerializerMixin):
    
    __tablename__ = 'doctors_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    specialty = db.Column(db.String)

    appointments = db.relationship('Appointment', back_populates='doctor')

    patients = association_proxy('appointments', 'patient')

    serialize_rules=["-appointments", "patients", "-patients.doctors"]

    


class Patient(db.Model, SerializerMixin):
    
    __tablename__ = 'patients_table'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    appointments = db.relationship('Appointment', back_populates='patient')

    doctors = association_proxy('appointments', 'doctor')

    serialize_rules = ("-appointments", "doctors", "-doctors.patients")


class Appointment(db.Model, SerializerMixin):
    
    __tablename__ = 'appointments_table'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors_table.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patients_table.id'))

    patient = db.relationship('Patient', back_populates='appointments')
    doctor = db.relationship('Doctor', back_populates='appointments' )

    serialize_rules = ["doctor.appointments", "patient.appointments"]