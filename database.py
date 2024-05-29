from flask import Flask
from models import db

def init_db(app: Flask):
    with app.app_context():
        db.create_all()
