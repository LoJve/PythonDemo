#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_
'''
@File    :    StrReprDemo.py
@Time    :    2019/03/14 08:47:35
@Author  :    Jayden Huang
@Version :    v1.0
@Contact :    Hjdong8@163.com
@Desc    :    __str__、__repr__ demo
'''

# Here put the import lib
class People(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "People object (name {0})".format(self.name)

p = People("Zhang") # p ==> <__main__.People object at 0x7f45fac38e10>
print(p)

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "People object (name {0})".format(self.name)
    __repr__ = __str__

s = Student("Li") # s ==> People object (name Li)
print(s)
