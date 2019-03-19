#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_
'''
@File    :    UnittestDemo2.py
@Time    :    2019/03/17 08:50:30
@Author  :    Jayden Huang
@Version :    v1.0
@Contact :    Hjdong8@163.com
@Desc    :    Unit test demo


对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过
'''

# Here put the import lib
import unittest
import sys,os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)

from Unittestdemo import Student


class TestStudent(unittest.TestCase):
    def test_80_to_100(self):
        s1 = Student('Li', 80)
        s2 = Student('Hu', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')
    
    def test_60_to_80(self):
        s1 = Student('Li', 60)
        s2 = Student('Hu', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')
    
    def test_0_to_60(self):
        s1 = Student('Li', 0)
        s2 = Student('Hu', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')
    
    def test_invalid(self):
        s1 = Student('Li', -1)
        s2 = Student('Hu', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError): # >>>Exception has occurred: SystemExit
            s2.get_grade()

if __name__ == "__main__":
    unittest.main()
