from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='template')
app.config.from_object(Config)
db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)