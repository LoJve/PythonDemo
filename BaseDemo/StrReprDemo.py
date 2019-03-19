#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_
'''
@File    :    StrReprDemo.py
@Time    :    2019/03/14 08:47:35
@Author  :    Jayden Huang
@Version :    v1.0
@Contact :    Hjdong8@163.com
@Desc    :    __str__、__repr__ demo
'''

# Here put the import lib
class People(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "People object (name {0})".format(self.name)

# p = People("Zhang") # p ==> <__main__.People object at 0x7f45fac38e10>
# print(p)

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "People object (name {0})".format(self.name)
    __repr__ = __str__

# s = Student("Li") # s ==> People object (name Li)
# print(s)

'''
    __iter__ demo
'''
class Fib(object):
    def __init__(self):
        self.a, self.b = 0,1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.b > 100:
            raise StopIteration()
        return self.b

# for index in Fib():
#     print(index)

'''
    __getitem__、__setitem__、__delitem__ demo
'''
class Fib2(object):
    def __init__(self):
        self.a, self.b = 0,1
        self["B"] = "BB"
        del self["B"]
    
    def __getitem__(self, n):
        self.a, self.b = 0,1
        if isinstance(n, int):
            for index in range(n):
                self.a, self.b = self.b, self.a + self.b
            return self.b
        elif isinstance(n, slice):
            self.L = []
            start = n.start
            stop = n.stop
            if not start:
                start = 0
            for index in range(stop):
                if(index >= start):
                    self.L.append(self.b)
                self.a, self.b = self.b, self.a + self.b
            return self.L
    
    def __setitem__(self, name, value):
        print('set {0} value {1}'.format(name, value))
    
    def __delitem__(self, name):
        print("del name {0}".format(name))

# f = Fib2()
# print(f[5])
# a = f[:7]
# print(a)

'''
    __getsttr__ demo
'''
class Student2(object):
    def __init__(self):
        self.name = "Li"
    
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        raise AttributeError('\'Student\' object has no attribute \'{0}\''.format(attr))

# s = Student2()
# print(s.score)
# print(s.age)

'''
    __getsttr__ demo 2
'''
class Chain(object):
    def __init__(self, path=''):
        self._path = path
    
    def __getattr__(self, path):
        return Chain('{0}/{1}'.format(self._path, path))

    def __call__(self, path):
        return Chain('{0}/{1}'.format(self._path, path))
    
    def __str__(self):
        return self._path
    __repr__ = __str__


print(Chain().status.user.timeline.list)
print(Chain().Users("Li").repos)

'''
    __call__ demo
'''
class Student3(object):
    def __init__(self, name=''):
        self._name = name
    
    def __call__(self):
        print('Name is {0}'.format(self._name))

s = Student3("Zhang")
s()
