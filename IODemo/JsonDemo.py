#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_
'''
@File    :    JsonDemo.py
@Time    :    2019/03/19 08:45:03
@Author  :    Jayden Huang
@Version :    v1.0
@Contact :    Hjdong8@163.com
@Desc    :    对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响
'''

# Here put the import lib
import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {"name": std.name, "age": std.age, "score": std.score}

def dict2student(s):
    return Student(s["name"], s["age"], s["score"])


# d = dict(name="Li", age=20, score=70)
# s = json.dumps(d)
# print(json.dumps(d))
# print(type(s))
# j = json.loads(s)
# print(j)
# print(type(j))

# s = Student("LI", 30, 80)
# sJson = json.dumps(s, default=student2dict)
# sJson2 = json.dumps(s, default=lambda s : s.__dict__)
# print(sJson)
# print(sJson2)
# dJson = json.loads(sJson, object_hook=dict2student)
# print(dJson)
# print(type(dJson))

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
j = json.loads(s)
print(j)
