from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from database import db
print(db)

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# if __name__ == '__main__':
#     app.run(debug=True)
