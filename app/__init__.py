# third-party imports
from flask import Flask,redirect,request,jsonify
from flask_cors import CORS, cross_origin
import os
import sqlite3
import logging
from logging import StreamHandler

# local imports

# Initialize application
app = Flask(__name__, instance_relative_config=True)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

read_replicas = ['https://dos-bazar-catalog-read-1.herokuapp.com','https://dos-bazar-catalog-read-2.herokuapp.com']
# read_replicas = ["http://127.0.0.1:5001","http://127.0.0.1:5002"]


#build database 
if(os.path.exists('bazar.db')):
    os.remove('bazar.db')

try:
    conn = sqlite3.connect('bazar.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE books
                (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                title varchar(64) NOT NULL,
                amount INTEGER NOT NULL)''')
    cursor.close()
    conn.close()
except :
    pass



#get routes
from app import routes

app_config = {
    'development': 'config.DevelopmentConfig',
    'production': 'config.ProductionConfig'
}

def create_app(config_name):
    app.config.from_object(app_config[config_name])
    file_handler = StreamHandler()
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)
    
    return app

