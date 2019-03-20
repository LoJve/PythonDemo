#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_
'''
@File    :    ThreadDemo1.py
@Time    :    2019/03/20 06:45:45
@Author  :    Jayden Huang
@Version :    v1.0
@Contact :    Hjdong8@163.com
@Desc    :    Python thread demo
'''

# Here put the import lib
import os

print('Process {0} start'.format(os.getpid()))
pid = os.fork()
if pid == 0:
    print('i am chlid process : {0} and my parent is {1}'.format(os.getpid(), os.getppid()))
else:
    print('I {0} just create a child process {1}'.format(os.getpid(), pid))
