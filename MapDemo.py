#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_
'''
@File    :    MapDemo.py
@Time    :    2019/03/13 06:54:05
@Author  :    Jayden Huang
@Version :    v1.0
@Contact :    Hjdong8@163.com
@Desc    :    利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
'''

# Here put the import lib
def normalize(name:str):
    return name.capitalize()

print(list(map(normalize, ['adam', 'LISA', 'barT'])))
