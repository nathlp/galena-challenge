from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Candidate(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    grup = db.Column(db.Integer, nullable=False)
    grupname = db.Column(db.String, nullable=False)
    cpf = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    adress = db.Column(db.String, nullable=False)

    def __init__(self):
        self.id 
        self.email 
        self.name 
        self.grup 
        self.grupname 
        self.cpf 
        self.phone
        self.birthday 
        self.adress 

    def construct(self, id, email, name, grup, grupname, cpf, phone, birthday, adress):
        self.id = id
        self.email = email
        self.name = name
        self.grup = grup
        self.grupname = grupname
        self.cpf = cpf
        self.phone = phone
        self.birthday = birthday
        self.adress = adress

    def list_all(self):
        candidates = Candidate.query.all()
        return candidates

    def list_one(self, id):
        candidate = Candidate.query.filter_by(id=id).first()
        return candidate
    
    def create(self, data):
        #teste = Candidate(2,'nathalia@gamil.com', "Nathalia lopes",11, 'grupo 11', '000.000.000-00', '1199999-9999','1999-06-22', "hfksdfhskdjfhdsjfhsdjfhsdfjhsdf ")
        for candidate in data:
            db.session.add(candidate)
            db.session.commit()
        
    def update(self, id):
        candidate = self.list_one(id)
        candidate.email 

    def delete(self, id):
        candidate = self.list_one(id)
        db.session.delete(candidate)
        db.session.commit()
        



    def __repr__(self):
        return f"{self.name}:{self.email}"


    
