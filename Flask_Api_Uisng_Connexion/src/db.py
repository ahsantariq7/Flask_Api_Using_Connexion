from src.extensions import db


def init_db():
    db.create_all()
