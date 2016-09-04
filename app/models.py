from app import db


class Kolom1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(140))

class Kolom2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(140))

class Kolom3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(140))

class KataSambung(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(140))
