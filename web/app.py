from flask import Flask, jsonify, request
import pymysql.cursors
import logging
import os
import json

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
        except Exception as e:
            r = None
        finally:
            connection.close()
    return jsonify({'posts' : r})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')


# Insert:
@app.route("/newpost", methods=['POST'])
def newpost():
    if request.method == 'POST':
        connection = connect_mysql()
        with connection.cursor() as cursor:
            try:
                query = "insert into `posts` (`post_title`) values (%s)"
                logging.warning('post_title')
                logging.warning(request.json['post_title'])
                cursor.execute(query, request.json['post_title'])
                connection.commit()
                return "Insert Successful"
            except Exception as e:
                logging.warning(e)
            finally:
                connection.close()