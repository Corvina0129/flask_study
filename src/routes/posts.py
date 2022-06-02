from flask import Blueprint


posts = Blueprint('posts', __name__)


@posts.route('/new', methods=['GET'])
def new_post():
    pass


@posts.route('/', methods=['POST'])
def create_post():
    pass


@posts.route('/', methods=['GET'])
def all_posts():
    pass


@posts.route('/<int:id>', methods=['DELETE'])
def remove_post():
    pass
