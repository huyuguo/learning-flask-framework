#coding:utf-8

from my_sqlalchemy import User, db

admin = User('admin', 'admin@example.com', 'good choice')
guest = User('guest', 'guest@example.com', 'good day')

db.session.add(admin)
db.session.add(guest)
db.session.commit()
