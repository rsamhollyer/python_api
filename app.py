from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from data.database import db
import os

app = Flask(__name__)
api = Api(app)
app.config.from_object("config.Config")

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=7698, debug=True)
