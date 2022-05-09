from datetime import datetime
from post import db

class User(db.Model):
    id = db.Column(db.Integer, primary=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(60), nullable=False)
    
class Post(db.Model):
    id = db.Column(db.Integer, primary=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.String(300), nullable=False)
    date = db.Column(db.String(60), nullable=False, default=datetime.utcnow)