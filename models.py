from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Siswa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    mapel = db.Column(db.String(100))
    nilai = db.Column(db.Integer)
