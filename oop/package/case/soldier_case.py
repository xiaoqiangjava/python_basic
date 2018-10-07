#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 士兵突击案例：演示一个类的属性可以是另一个类的对象
# python中判断一个对象是不是None使用身份运算符is/is not
# is是判断两个对象的内存地址是否相同，==是判断两个变量的值是否相等


class Gun:
    """
    枪类：枪有型号和子弹数量
    """

    def __init__(self, model):
        """
        初始化枪的属性
        :param model: 枪的型号
        """
        # 枪的型号
        self.model = model
        # 子弹数量
        self.bullet_count = 0

    def add_bullet(self, count):
        """
        添加子弹
        :param count: 子弹数量
        :return:
        """
        self.bullet_count += count

    def shoot(self):
        """
        射击方法
        :return:
        """
        # 判断枪中有没有子弹
        if self.bullet_count <= 0:
            print("%s没子弹了" % self.model)
            return

        self.bullet_count -= 3
        print("[%s]突突突。。。[%s]" % (self.model, self.bullet_count))


class Soldier:
    """
    士兵类
    """

    def __init__(self, name):
        """
        初始化属性
        :param name: 士兵的名字
        """
        self.name = name
        # 枪：新兵没有枪
        self.gun = None

    def fire(self):
        """
        开火
        :return:
        """
        # 判断士兵有没有枪
        if self.gun is None:
            print("%s还没有枪" % self.name)
            return
        # 发出口号
        print("冲啊。。。[%s]" % self.name)
        # 给枪填满子弹
        self.gun.add_bullet(40)
        # 让枪发射子弹
        self.gun.shoot()


# 创建枪对象
ak47 = Gun("AK47")

# 创建士兵
xusanduo = Soldier("许三多")
xusanduo.gun = ak47
xusanduo.fire()
