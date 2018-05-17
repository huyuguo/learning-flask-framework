# coding:utf-8

# Python中函数也是对象, 可以赋值给其他对象
def shout(word='yes'):
  return word.capitalize() + '!'


print(shout())

scream = shout

print(scream())

del shout

try:
  print(shout())
except NameError as e:
  print(e)

print(scream())

# 函数它可以在其他函数里面定义
print('##########################')


def talk():
  def whisper(word='yes'):
    return word.lower() + '...'

  print(whisper())


talk()

try:
  print(whisper())
except NameError as e:
  print(e)

# 可以赋值给其他变量
# 可以在其它函数里面定义

print('##########################')


# 一个函数可以被另一个函数return

def getTalk(kind='shout'):
  def shout(word='yes'):
    return word.capitalize() + '!'
  def whisper(word='yes'):
    return word.lower() + '...'

  if kind == 'shout':
    return shout
  else:
    return whisper

talk = getTalk()
print(talk)
print(talk())
print(getTalk('whisper')())

print('##########################')
# 既然你可以return一个函数，你就可以把一个函数当参数传递:

def doSomethingBefore(func):
  print('I do something before then I call the function you gave me')
  print(func())

doSomethingBefore(scream)
# 输出为:
# I do something before then I call the function you gave me
# Yes!

print('----------------------------')
# 手动创建装饰器
# 装饰是一个函数，该函数需要另一个函数作为它的参数
def my_shiny_new_decorator(a_function_to_decorator):
  def the_wrapper_around_the_original_function():
    # 在这里放置你想在原来函数执行前执行的代码
    print('Before the function runs')
    # 调用原来的函数(使用圆括号)
    a_function_to_decorator()
    # 在这里放置你想在原来函数执行后执行的代码
    print('After the function runs')
  return the_wrapper_around_the_original_function

def a_stand_alone_function():
  print("I am a stand alone function, don't you dare modify me")

a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)

a_stand_alone_function()

@my_shiny_new_decorator
def another_stand_alone_function():
  print('Leave me alone')
another_stand_alone_function()