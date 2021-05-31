import sys
sys.path.insert(0, '.')
from data.database import db


class BuildingModel(db.Model):
    __tablename__ = "buildings"

    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(255))
