from flask import Flask
from flask.ext.restful import Api
app = Flask(__name__)
restful_api = Api(app)

from api import dispatcher
