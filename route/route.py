#coding:utf-8
from app import app
from flask import  request

@app.route('/', methods=['GET'])
def hello_world():
  print(request.query_string)
  print(request.args)

  name = request.args.get('name')
  age = request.args.get('age', 0 , int)
  print(name, age)

  # b'name=huyuguo&age=100'
  # ImmutableMultiDict([('name', 'huyuguo'), ('age', '100')])
  # huyuguo 100
  return 'Hello World xxx xxx!'

@app.route('/hello', methods=['POST'])
def hello():
  print(request.data)
  return 'Hello'