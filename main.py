import sqlite3 
from flask import Flask, jsonify, request
from crud import *
app = Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    rows = get_data_from_db('SELECT * FROM posts')
    posts_data = []
    for row in rows:
        posts_data.append({
            'id': row[0],
            'title': row[1],
            'subtitle': row[2],
            'slug': row[3],
            'content': row[4],
            'created_on': row[5]
        })
    return jsonify(posts_data)

@app.route("/post_add", methods=['POST'])
def post_add():
    post_title = request.values['title']
    post_subtitle = request.values['subtitle']
    post_slug = request.values['slug']
    post_content = request.values['content']
    post_created_on = request.values['created_on']
    
    get_data_from_db('INSERT INTO posts (title,subtitle,slug,content,created_on) VALUES (?,?,?,?,?)', (post_title,post_subtitle,post_slug,post_content,post_created_on))

    return jsonify({'id':"Tamamlandı"})

@app.route("/post-delete/<id>", methods=['DELETE'])
def post_delete(id):
    get_data_from_db()('DELETE FROM posts WHERE id=?',(id,))
    return jsonify(id,"Silme işlemi tamamlandı")


@app.route('/post_read')
def read():
    rows = get_data_from_db('SELECT * FROM posts')
    posts = []
    for row in rows:
        posts.append({
            'title': row[0],
            'subtitle': row[1],
            'slug': row[2],
            'contend': row[3],
            'created_on': row[4],
            'id':row[5]
        })
    return jsonify(posts)

@app.route("/update/<id>", methods=['POST'])
def post_update(id):
    post_title = request.args.get('title')
    post_subtitle = request.args.get('subtitle')
    post_slug = request.args.get('slug')
    post_content = request.args.get('content')
    post_created_on = request.args.get('created_on')

    get_data_from_db('UPDATE posts SET title=?, subtitle=?, slug=?, content=?, created_on=? WHERE id=?', (post_title, post_subtitle, post_slug,post_content,post_created_on, id))
 
    return jsonify(durum="Güncelleme işlemi tamamlandi")





@app.route("/post_read/<id>", methods=['GET'])
def read_id(id):

    row = get_data_from_db('SELECT * FROM posts WHERE id=?', (id,))

    if len(row)==0:
        return None
    posts_data = {
        'id': row[0][0],
        'title': row[0][1],
        'subtitle': row[0][2],
        'slug': row[0][3],
        'content': row[0][4],
        'created_on': row[0][5]
        }
    return jsonify(posts_data)
app.run()