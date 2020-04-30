import flask
from flask import request

server = flask.Flask(__name__)


@server.route('/login', methods=['get', 'post'])
def login():

    username = request.values.get('username')

    pwd = request.values.get("pwd")

    if username and pwd:
        if username == 'zhuxingyue' and pwd == '111':

            return "login success!!"
        else:

            return "login fail!!"
    else:
        return "param is faile"


if __name__ == "__main__":
    server.run(debug=True, port=9888, host='127.0.0.1')
