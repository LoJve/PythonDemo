#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_
'''
@File    :    MultiProcessDemo.py
@Time    :    2019/03/20 06:53:42
@Author  :    Jayden Huang
@Version :    v1.0
@Contact :    Hjdong8@163.com
@Desc    :    Multiprocess demo
'''

# Here put the import lib
import multiprocessing
import time

def worker(interval):
    n = 5
    while n > 0:
        print('The time is {0}'.format(time.ctime()))
        time.sleep(interval)
        n -= 1

if __name__ == "__main__":
    p = multiprocessing.Process(target=worker, args=(3,))
    p.start()
    print('p.pid = {0}'.format(p.pid))
    print('p.name = {0}'.format(p.name))
    print('p.is_alive = {0}'.format(p.is_alive))
