#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_
'''
@File    :    DecoratorDemo.py
@Time    :    2019/03/13 09:54:28
@Author  :    Jayden Huang
@Version :    v1.0
@Contact :    Hjdong8@163.com
@Desc    :    Decorator demo

请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
'''

# Here put the import lib
from datetime import datetime
import time

def metric(fn):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = fn(*args, **kwargs)
        end = datetime.now()
        print('%s executed in %s ms' % (fn.__name__, end - start))
        return result
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


# import functools
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             print('{1} {0}()'.format(func.__name__, text))
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator

# @log("Excute")
# def now():
#     print('2019-3-14')
# f = now
# f()
# print(f.__name__)
