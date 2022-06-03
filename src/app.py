from routes.posts import posts

from settings import app, db

app.register_blueprint(posts, url_prefix='/posts')
db.create_all()


if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )
