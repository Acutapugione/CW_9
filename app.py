from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import json

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# with open('data/database.json', 'r') as file_base:
#     base = json.load(file_base)



import routes, forms, models