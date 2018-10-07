#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 小明爱跑步案例


class Persion:
    """
    该类是一个人类，有name和weight两个属性
    """

    def __init__(self, name, weight):
        """
        初始化对象方法
        :param name: 姓名
        :param weight: 体重
        """
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫%s, 我的体重是%.2f" % (self.name, self.weight)

    def run(self):
        """
        跑步方法，跑步可以使体重减0.5
        :return:
        """
        self.weight -= 0.5
        print("%s爱跑步，跑步使体重减少0.5kg" % self.name)

    def eat(self):
        """
        吃东西方法，吃东西使体重增加0.6kg
        :return:
        """
        self.weight += 0.6
        print("%s是吃货，吃完这顿再减肥" % self.name)


xiaoming = Persion("xiaoming", 62.5)
xiaoming.run()
xiaoming.eat()
print(xiaoming)

# 同一类中创建的多个对象，属性之间相互不干扰
xiaomei = Persion("xiaomei", 45.5)
xiaomei.run()
xiaomei.eat()
print(xiaomei)
