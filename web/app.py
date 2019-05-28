from flask import Flask
from flask import jsonify
import pymysql.cursors
import logging
import os

def connect_mysql():
    connection = pymysql.connect(host=os.environ['MYSQL_HOST_NAME'],
                                user=os.environ['MYSQL_USERNAME'],
                                password=os.environ['MYSQL_PASSWORD'],
                                db=os.environ['MYSQL_DATABASE'],
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    return connection

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized template test2'

@app.route('/posts')
def posts():
    connection = connect_mysql()
    with connection.cursor() as cursor:
        try:
            sql = "SELECT * FROM posts"
            cursor.execute(sql)
            r = cursor.fetchall()
            for row in r:
                print('row')
                print(r)
        except Exception as e:
            r = None
    return jsonify({'posts' : r})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')