#coding:utf-8
from app import app, socketio, db
import route.route
import model.model

if __name__ == '__main__':
  socketio.run(app)