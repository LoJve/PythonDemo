#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_
'''
@File    :    SortedDemo.py
@Time    :    2019/03/13 08:54:57
@Author  :    Jayden Huang
@Version :    v1.0
@Contact :    Hjdong8@163.com
@Desc    :    
假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

请用sorted()对上述列表分别按名字排序：
'''

# Here put the import lib

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()

print(sorted(L, key=by_name, reverse=True))
