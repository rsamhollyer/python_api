from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from data.db import db
import os

print(CORS)
basedir = os.path.join(
    os.path.dirname(
        os.path.abspath(
            os.path.dirname(__file__))),
    '/data/data.db')

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{basedir}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


if __name__ == '__main__':
    app.run(debug=True)
