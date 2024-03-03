from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='http://localhost:3000')

UPLOADER_FOLDER = 'image'
app.config['UPLOAD_FOLDER'] = UPLOADER_FOLDER

from app import routes

