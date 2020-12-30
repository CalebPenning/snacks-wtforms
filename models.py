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
    
    name = db.Column(db.String(30),
                     nullable=False,
                     unique=False)
    
    price = db.Column(db.Float,
                      nullable=False,
                      unique=False)
    
    