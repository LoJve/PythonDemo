#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_
'''
@File    :    LambdaDemo.py
@Time    :    2019/03/13 09:46:14
@Author  :    Jayden Huang
@Version :    v1.0
@Contact :    Hjdong8@163.com
@Desc    :    请用匿名函数改造下面的代码：
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
'''

# Here put the import lib
L = list(filter(lambda x : x % 2 ==1, range(1, 20)))
print(L)
