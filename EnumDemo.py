#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_
'''
@File    :    EnumDemo.py
@Time    :    2019/03/17 00:52:30
@Author  :    Jayden Huang
@Version :    v1.0
@Contact :    Hjdong8@163.com
@Desc    :    把Student的gender属性改造为枚举类型，可以避免使用字符串：
'''

# Here put the import lib
# -*- coding: utf-8 -*-
from enum import Enum

class Gender(Enum):
    male = 0,
    female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

s = Student("Zhang", Gender.male)
print(s.gender)
s2 = Student("Zhang", "man")
print(s2.gender)

