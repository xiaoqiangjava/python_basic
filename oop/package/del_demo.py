#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 创建的对象在销毁前会调用__del__()方法


class Cat:
    """
    __del__()方法演示: 如果在对象销毁前想对对象做一些事情可以在这个函数中处理
    """
    def __init__(self, name):
        print("初始化方法，创建对象后执行")
        self.name = name

    def __del__(self):
        print("对象销毁之前会自动调用")


# tom是一个全局变量
tom = Cat("Tom")
# del()函数可以删除一个对象
del tom
print("-" * 50)
