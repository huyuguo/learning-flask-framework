#coding:utf-8

from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)

socketio = SocketIO(app)

# TODO
print(config.Config.SQLALCHEMY_DATABASE_URI)

if __name__ == '__main__':
  socketio.run(app)
