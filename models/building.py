# import sys
# sys.path.insert(0, '.')
from data.database import *
from flask import jsonify

print(db, ma)


class BuildingModel(db.Model):
    __tablename__ = "buildings"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    street = db.Column(db.String(50), nullable=False)
    building_number = db.Column(db.String(12), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    zipcode = db.Column(db.String(12), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    country_code = db.Column(db.String(50), nullable=False)
    latitude = db.Column(db.Float(20), nullable=False)
    longitude = db.Column(db.Float(20), nullable=False)
    isHq = db.Column(db.Boolean, nullable=False)

    # people = db.relationship("PersonModel", lazy='select', backref='id')

    def __init__(
            self,
            street,
            building_number,
            city,
            zipcode,
            country,
            country_code,
            latitude,
            longitude, isHq):
        self.street = street
        self.building_number = building_number
        self.city = city
        self.zipcode = zipcode
        self.country = country
        self.country_code = country_code
        self.latitude = latitude
        self.longitude = longitude
        self.isHq = isHq
    # def


class BuildingSchema(ma.Schema):
    class Meta:
        model = BuildingModel
