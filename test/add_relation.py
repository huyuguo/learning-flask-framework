#coding:utf-8

from my_sqlalchemy import Post, Category, db

py = Category('Python')
print(py)

p = Post('Hello Python!', 'Python is pretty cool', py)
db.session.add(py)
db.session.add(p)

db.session.commit()

print(py.posts.all())
