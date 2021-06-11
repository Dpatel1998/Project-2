from application import db

class Soldier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nationality = db.Column(db.String(30), nullable=False)
    player_class = db.Column(db.String(30), nullable=False)
    build = db.Column(db.String(255), nullable=False)