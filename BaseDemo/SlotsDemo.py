#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_
'''
@File    :    SlotsDemo.py
@Time    :    2019/03/14 07:45:59
@Author  :    Jayden Huang
@Version :    v1.0
@Contact :    Hjdong8@163.com
@Desc    :    __slots__ demo
'''

# Here put the import lib
class People(object):
    __slots__ = ('name', 'age') #用tuple定义允许绑定的属性名称,只对当前类有效，对子类无效

p = People()
p.name = "Zhang"
p.age = 12
# p.score = 60    # 'People' object has no attribute 'score'

class Student(People):
    pass
s = Student()
s.name = "Zhang"
s.age = 12
s.score = 60
print(s.score)
