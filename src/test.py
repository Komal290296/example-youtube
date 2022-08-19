from flask import Flask
from flask_cors import CORS

class ServiceGenerator:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)