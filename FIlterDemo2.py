#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_
'''
@File    :    FIlterDemo2.py
@Time    :    2019/03/13 08:40:32
@Author  :    Jayden Huang
@Version :    v1.0
@Contact :    Hjdong8@163.com
@Desc    :    回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
'''

# Here put the import lib
def is_palindrome(x):
    return x == int(str(x)[::-1])

def get_num_of_times():
    return list(filter(is_palindrome, range(1, 200)))

print(get_num_of_times())

