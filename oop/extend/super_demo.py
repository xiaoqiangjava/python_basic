#! /usr/bin/python
# -*- encoding: utf-8 -*-

# super是python中的一个特殊类，可以使用该类的对象对用父类中原本的方法，可以达到扩展父类
# 方法的实现，即子类即要包含父类的功能，又要新增功能实现，可以使用super().方法名()调用父类方法
# super()就是super类创建的对象，在python中创建对象就是：类名()，跟Java不同的是缺少new关键字
# 所以在开发时遇到类似super()要能考虑到时类创建的对象，而不是方法的调用
# 注意：在python中调用父类方法还有一种方式：父类名.方法(self), 不推荐使用，而且类名写错时会出现死循环


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
        # 使用super()对象调用父类原本的方法实现
        # Dog.bark(self), 参数self不能省略。当把类名写成：Xiaotianquan.bark(self)时会形成死循环
        super().bark()
        print("%s叫的跟神一样" % self.name)


# 创建对象
xtq = Xiaotianquan("哮天犬")
# 如果在子类中重写了父类的方法，那么使用子类对象调用方法时，会调用子类中重写之后的方法
xtq.bark()
xtq.fly()
