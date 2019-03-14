#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_
'''
@File    :    PropertyDemo.py
@Time    :    2019/03/14 07:53:09
@Author  :    Jayden Huang
@Version :    v1.0
@Contact :    Hjdong8@163.com
@Desc    :    请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
'''

# Here put the import lib
class Screen(object):
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value
    
    @property
    def resolution(self):
        return self._height * self._width

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')


