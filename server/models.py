from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship  # Import relationship
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy_serializer import SerializerMixin  # Import SerializerMixin
from datetime import datetime

db = SQLAlchemy()

class Bakery(db.Model, SerializerMixin):  # Inherit from SerializerMixin
    __tablename__ = 'bakery'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Define a relationship to BakedGood
    baked_goods = relationship('BakedGood', back_populates='bakery')

    def to_dict(self):
        # Serialize relationships using SerializerMixin
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'baked_goods': [bg.to_dict() for bg in self.baked_goods],  # Serialize baked goods
        }

class BakedGood(db.Model, SerializerMixin):  # Inherit from SerializerMixin
    __tablename__ = 'baked_good'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Define a foreign key to link BakedGood to Bakery
    bakery_id = db.Column(db.Integer, db.ForeignKey('bakery.id'))
    
    # Define a relationship to Bakery
    bakery = relationship('Bakery', back_populates='baked_goods')

    def to_dict(self):
        # Serialize relationships using SerializerMixin
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'created_at': self.created_at,
        }
