#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_
'''
@File    :    Unittestdemo.py
@Time    :    2019/03/17 08:22:30
@Author  :    Jayden Huang
@Version :    v1.0
@Contact :    Hjdong8@163.com
@Desc    :    Unit test demo

对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过
'''

# Here put the import lib

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def get_grade(self):
        if self.score < 0 or self.score > 100:
            raise ValueError('Value error: not in range from 0 to 100')
        if self.score >= 80 :
            return 'A'
        elif self.score >= 60 :
            return 'B'
        else:
            return 'C'
            


