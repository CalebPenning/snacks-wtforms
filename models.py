"""Models for our intermediate-flask demo project"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
class Snack(db.Model):
    """Snacks, baby."""
    
    __tablename__ = "snacks"
    
    def __repr__(self):
        s = self
        return f"<Snack id = {s.id}, Snack name = {s.name}, Snack price = {s.price}>"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
        
    email = db.Column(db.String(50),
                      nullable=False,
                      unique=False)    
    
    name = db.Column(db.String(30),
                     nullable=False,
                     unique=False)

    category = db.Column(db.String(20),
                         nullable=False,
                         unique=False)
    
    price = db.Column(db.Float,
                      nullable=False,
                      unique=False)
    
    is_healthy = db.Column(db.Boolean,
                           nullable=False,
                           unique=False)
    
    quantity = db.Column(db.Integer,
                         nullable=False,
                         unique=False)
    
    unit_measure = db.Column(db.String(25),
                             nullable=False,
                             unique=False)

    