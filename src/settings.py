from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

app.config['HOST'] = '127.0.0.1'
app.config['PORT'] = 8080
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

