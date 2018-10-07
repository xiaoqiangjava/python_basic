#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 多态：不同的子类调用父类的同一个方法，具有不同的行为

# 创建对象的过程也叫对象的实例化：每一个对象都有自己的内存空间保存各自的属性，而多个对象的方法在内存中只有一份
# 调用方法时需要把对象的引用传递到方法内部


class Dog(object):
    """
    狗类，是所有狗的父类
    """

    def __init__(self, name):
        """
        初始化类属性
        :param name: 名字
        """
        self.name = name

    def play(self):
        print("%s 蹦蹦跳跳的玩耍" % self.name)


class XiaotDog(Dog):
    """
    哮天犬类
    """

    def play(self):
        print("%s 飞到天上去玩耍" % self.name)


class Person(object):
    """
    人类
    """

    def __init__(self, name):
        """
        初始化类舒心
        :param name: 姓名
        """
        self.name = name

    def play_with_dog(self, dog):
        """
        人和狗玩耍
        :param dog:
        :return:
        """
        print("%s 和 %s 玩耍快乐的玩耍" % (self.name, dog.name))


# 创建人类对象
person = Person("xiaoqiang")
dog = Dog("旺财")
dog.play()
person.play_with_dog(dog)
dog = XiaotDog("哮天犬")
dog.play()
person.play_with_dog(dog)
