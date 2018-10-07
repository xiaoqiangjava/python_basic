#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 类是一个对象，不尽有类属性，也会有类方法
# 类方法需要用修饰器@classmethod来标识，告诉python解释器这是一个类方法，而不是实例方法，类方法的第一个参数时cls
# 类方法可以访问类的属性


class Tool(object):

    # 使用赋值语句给类属性赋值，记录该类创建的对象个数
    count = 0

    # 定义类方法
    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量：%d" % cls.count)

    def __init__(self, name):
        """
        初始化对象的属性
        :param name: 名称
        """
        self.name = name
        # 类名.属性的方式访问类属性
        Tool.count += 1


# 创建对象
tool1 = Tool("斧头")
tool2 = Tool("石头")
tool3 = Tool("铁锹")
Tool.show_tool_count()
