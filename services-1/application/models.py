from application import db

class Soldier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nationality = db.Column(db.String(30),nullable=False)
    soldier_class = db.Column(db.String(30),nullable=False)
    build = db.Column(db.String(500),nullable=False)