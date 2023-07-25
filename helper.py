import sqlite3
from flask import jsonify, Flask,request
from crud import get_data_from_db

app= Flask(__name__)



@app.route('/delete/<int=id>', methods = "DELETE")
def delete(id):
    get_data_from_db('DELETE FROM posts WHERE id=?',(id,))

    return jsonify('Halletim')



@app.route('/read/<id>')
def read(id):
    rows = get_data_from_db('SELECT * FROM posts WHERE id=?',(id,))
    posts = []
    for row in rows:
        posts.append(
            {
                'id': row[0],
                'title': row[1],
                'subtitle': row[2],
                'slug': row[3],
                'content': row[4],
                'created_on': row[5]
            }
        )

    return posts


@app.route('/add', methods=['POST'])
def add():
    post_title = request.values['title']
    post_subtitle=request.values['subtitle']
    post_slug=request.values['slug']
    post_content=request.values['content']


    get_data_from_db('INSERT INTO posts (title,subtitle,slug,content) VALUES (?,?,?,?)',(post_title,post_subtitle,post_slug,post_content))
    return jsonify({'id': 'kaydedildi'})

@app.route('/update/<id>', methods = ['PUT'])
def update(id):
    post_title = request.values['title']
    post_subtitle=request.values['subtitle']
    post_slug=request.values['slug']
    post_content=request.values['content']
    get_data_from_db('UPDATE posts SET title=?, subtitle=?, slug=?, content=? WHERE id=?', (post_title,post_subtitle,post_slug,post_content,id))
    return jsonify('hallettim')


app.run()