#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 当子类的方法实现和父类的方法实现不一样时，可以重写父类的方法


class Animal:
    """
    动物类：是所有动物的父类，有吃、喝、跑、睡四个方法
    """

    def __init__(self, name):
        """
        初始化类中的属性
        :param name:
        """
        self.name = name

    def eat(self):
        print("%s吃" % self.name)

    def drink(self):
        print("%s喝" % self.name)

    def run(self):
        print("%s跑" % self.name)

    def sleep(self):
        print("%s睡" % self.name)


class Dog(Animal):
    """
    狗类，继承Animal父类
    """

    def bark(self):
        print("%s旺旺叫" % self.name)


class Xiaotianquan(Dog):
    """
    哮天犬类，哮天犬可以飞
    """

    def fly(self):
        print("%s 会飞" % self.name)

    def bark(self):
        """
        重写父类中的brak()方法
        :return:
        """
        print("%s叫的跟神一样" % self.name)


# 创建对象
xtq = Xiaotianquan("哮天犬")
# 如果在子类中重写了父类的方法，那么使用子类对象调用方法时，会调用子类中重写之后的方法
xtq.bark()
xtq.fly()
