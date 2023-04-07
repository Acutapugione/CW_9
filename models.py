from app import app, db


class User(db.Model):  
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    login = db.Column(
        db.String(80),
        nullable=False,
        unique=True    
    )  
    password = db.Column(
        db.String(50),
        nullable=False
    )