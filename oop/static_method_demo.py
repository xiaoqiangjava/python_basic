#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 静态方法：当一个方法既不访问实例属性，也不需要访问类属性时，可以将方法定义为静态方法
# 静态方法不用传第一个参数cls或者self


class Tool(object):
    """
    静态方法演示
    """

    @staticmethod
    def demo():
        print("这是一个静态方法，既不访问实例属性，也不访问类属性")


# 访问静态方法：类名.
Tool.demo()
