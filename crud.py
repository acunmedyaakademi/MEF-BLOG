from flask import jsonify, Flask,request
import sqlite3

def get_data_from_db(query, params = tuple()):
    conn = sqlite3.connect('post.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    print(" Q : ",query)
    print(params)
    cursor.execute(query, params)
    #rows = cursor.fetchall()
    rows = cursor.fetchone()
    conn.commit()
    conn.close()

    return (rows)

def get_index_data():
    conn = sqlite3.connect('post.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM posts')
    #rows = cursor.fetchall()
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows
