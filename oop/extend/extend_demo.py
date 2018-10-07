#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 继承：子类具有父类的所有属性和方法
# 语法：class 类名(父类名)：
# 继承时也会继承父类的__init__()方法，如果父类有属性需要初始化，那么子类也需要初始化该属性
# 继承具有传递性
# 父类中的私有属性和私有方法不能在继承的子类中访问


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


class Cat(Animal):
    """
    猫类：会抓老鼠
    """

    def catch(self):
        print("%s 会抓老鼠" % self.name)


# 创建对象
wangcai = Dog("旺财")
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()

xtq = Xiaotianquan("哮天犬")
xtq.fly()
xtq.bark()

tom = Cat("Tom")
tom.catch()
