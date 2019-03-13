#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_
'''
@File    :    TestDemo1.py
@Time    :    2019/03/10 10:09:35
@Author  :    Jayden Huang
@Version :    v1.0
@Contact :    Hjdong8@163.com
@Desc    :    杨辉三角
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1] 
'''

# Here put the import lib

def set_yanghui(num):
    result = [1]
    index = 1
    while index <= num:
        yield result
        result = [1] + [result[i] + result[i + 1] for i in range(len(result) - 1)] + [1]
        index += 1

rlt = set_yanghui(10)    
for result in rlt:
    print(result)

