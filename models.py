from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # 'admin' or 'customer'
    bills = db.relationship('Bill', backref='user', lazy=True)

    def __repr__(self):
        return f'<User  {self.name}>'

class Bill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bill_date = db.Column(db.String(10), nullable=False)  # Format: YYYY-MM-DD
    bill_amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Bill {self.id} for User {self.user_id}>'