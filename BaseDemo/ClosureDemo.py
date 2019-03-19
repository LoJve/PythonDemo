#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_
'''
@File    :    ClosureDemo.py
@Time    :    2019/03/13 09:17:26
@Author  :    Jayden Huang
@Version :    v1.0
@Contact :    Hjdong8@163.com
@Desc    :    利用闭包返回一个计数器函数，每次调用它返回递增整数
'''

# Here put the import lib
def createCounter():
    index = [0]
    def counter():
        index[0] = index[0] + 1
        return index[0]
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())