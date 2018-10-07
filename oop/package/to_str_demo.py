#! /usr/bin/python
# -*- encoding: utf-8 -*-

# __str__方法，相当于Java中的toString()方法


class Cat:
    """
    __str__方法演示：可以定制打印对象的输出值
    """
    def __init__(self, name):
        print("初始化方法")
        self.name = name

    def __del__(self):
        print("对象销毁前调用")

    def __str__(self):
        """
        该方法必须返回一个字符串
        :return:
        """
        return "Cat[name=%s]" % self.name


tom = Cat("Tom")
print(tom)
