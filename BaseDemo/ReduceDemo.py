#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_
'''
@File    :    ReduceDemo.py
@Time    :    2019/03/13 07:03:14
@Author  :    Jayden Huang
@Version :    v1.0
@Contact :    Hjdong8@163.com
@Desc    :    将字符创‘13579’转为int类型13579
'''

# Here put the import lib
from functools import reduce

my_dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def str2int(sNum):
    def change2int(x, y):
        return x * 10 + y
    def char2int(cNum):
        return my_dict[cNum]
    return reduce(change2int, map(char2int, sNum))

print(str2int('13579'))
