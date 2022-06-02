from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from routes.posts import posts

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['HOST'] = '127.0.0.1'
app.config['PORT'] = 8080
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./posts.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.register_blueprint(posts, url_prefix='/posts')

db.create_all()


if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )
