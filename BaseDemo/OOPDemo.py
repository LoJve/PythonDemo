#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_
'''
@File    :    OOPDemo.py
@Time    :    2019/03/14 07:38:14
@Author  :    Jayden Huang
@Version :    v1.0
@Contact :    Hjdong8@163.com
@Desc    :    为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加
'''

# Here put the import lib
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

