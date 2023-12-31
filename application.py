import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from crud import get_data_from_db,get_index_data
from helpers import commentForm,getProfilePicture
from flaskwebgui import FlaskUI
from app import app


def get_post(post_id):
    post = get_data_from_db(query='SELECT * FROM posts WHERE id = ?',params=(post_id,))
    if post is None:
        abort(404)
    return post

application = Flask(__name__)
application.config['SECRET_KEY'] = 'secretsecretsecretkey'


"""@application.route('/')
def index():
    posts = get_index_data()
    print("POSTS ",posts)
    return render_template('basic_blog.html', posts=posts)
"""
@application.route('/')
def index():
    posts = get_index_data()
    print("POSTS ",posts)
    return render_template('index.html', posts=posts)


@application.route('/<post_id>')
def post(post_id):
    print("WOOOORKING")
    post = get_post(post_id)
    form = commentForm(request.form)
    comments = get_data_from_db(query='select * from comments where post = ?',params=(post_id,))
    return render_template('post.html', post=post,posts = get_index_data(),
                            id=post[0],
                title=post[1],
                tags=post[2],
                content=post[3],
                author=post[4],
                views=post[7],
                date=post[5],
                time=post[6],
                form=form,
                comments=comments,
                )


#Important Create Post Function --------------------------------
@application.route('/editor/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            
            get_data_from_db(query='INSERT INTO posts (title, content) VALUES (?, ?)',params=(title, content))
            return redirect(url_for('index'))

    return render_template('create.html')


#Edit Post Function -------

@application.route("/<int:id>/editor/edit", methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            get_data_from_db(query='UPDATE posts SET title = ?, content = ? WHERE id = ?',
                         params=(title, content, id))
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


# The Delete Function -----------------------------------
@application.route('/<int:id>/editor/delete', methods=['POST','GET'])
def delete(id):
    post = get_post(id)
    get_data_from_db(query='DELETE FROM posts WHERE id = ?',params=(id,))
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
