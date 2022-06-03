from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
)

from db_models.post import Post
from settings import db


posts = Blueprint('posts', __name__)


@posts.route('/new', methods=['GET'])
def new_post():
    return render_template('new.html')


@posts.route('/', methods=['POST'])
def create_post():
    form = request.form
    post = Post(form['title'], form['body'])
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('posts.new_post'))


@posts.route('/', methods=['GET'])
def all_posts():
    posts = Post.query.order_by(Post.id).all()
    return render_template('allposts.html', posts=posts)


@posts.route('/<int:id>', methods=['DELETE'])
def remove_post(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('posts.all_posts'))
