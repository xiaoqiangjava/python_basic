#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 在一个类中定义私有属性和私有方法
# 在方法名或者属性名前面加__age，那么该方法或属性就是私有的


class Woman:
    """
    女人类：女人的年龄和秘密是私有的，不能再外部访问
    """

    def __init__(self, name, age):
        """
        初始化类的属性型
        :param name: 姓名
        :param age: 年龄
        """
        self.name = name
        self.__age = age

    def __secret(self):
        """
        秘密方法
        :return:
        """
        # 在类的内部可以访问私有属性和私有方法
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiaomei = Woman("小美", 18)
print(xiaomei.name)

# 在python中没有真正的私有，当在方法或者属性前面添加了__后python解释器会对该方法或者属性
# 进行特殊的处理：_类名__方法名，在实际开发中不建议使用这种方式访问私有属性和方法
xiaomei._Woman__secret()
