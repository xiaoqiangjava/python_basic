#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 类的初始化方法：定义一个类的时候定义这个类包含哪些属性
# 类名()创建对象时做了两件事：1. 在内存中分配空间。2. 调用初始化方法__init__为对象的属性设置初始值


class Cat:
    """
    __init__方法演示：使用类名()创建对象时会自动调用__init__()方法
    """
    def __init__(self, name):
        """
        该方法的作用是在定义类的时候指定这个类具有哪些属性
        可以通过self.属性名 = 属性的初始值给对象设置属性
        """
        print("这是初始化方法，在创建对象时自动调用")
        self.name = name

    def eat(self):
        print("%s爱吃鱼" % self.name)


tom = Cat("Tom")
print(tom.name)
tom.eat()
lazy_cat = Cat("大懒猫")
lazy_cat.eat()
