#coding:utf-8
from my_sqlalchemy import User

users = User.query.all()
print(users)

admin = User.query.filter_by(username='admin').first()

print(admin)

print(User.query.limit(1).first())

print(User.query.get_or_404(22))