#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_
'''
@File    :    PartialDemo.py
@Time    :    2019/03/13 10:12:30
@Author  :    Jayden Huang
@Version :    v1.0
@Contact :    Hjdong8@163.com
@Desc    :    Partial Demo
'''

# Here put the import lib
from functools import partial
s_10 = '123'

a_2 = int(s_10, base=4)
print("int = ", a_2)

func = partial(int, base=4)
print("func = ", func(s_10))

