#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 单例模式：一个类在对象中创建的对象只有唯一一个，即创建的所有对象的内存地址相同
# 创建对象：类()做了两件事：
# 1. 调用__new__()为对象分配内存空间, 并返回分配空间的对象引用，传递给__init__()方法
# 2. 调用__init__()方法初始化对象属性
# 2. 单例模式可以定义一个类属性init_flag记录是否执行过初始化操作实现初始化代码只执行一次


class MusicPlayer(object):
    """
    单例模式：单例模式需要重新__new__()方法， 该方法必须要返回super().__new__(cls)
    """
    # 定义类属性，记录第一个创建出来的对象引用
    instance = None
    # 初始化标识符
    init_flag = False

    def __new__(cls, *args, **kwargs):
        """
        重写父类分配空间方法
        :param args:
        :param kwargs:
        :return: 对象的引用
        """
        # 创建对象时，__new__()方法会自动调用
        print("创建对象，分配空间")
        # 当类属性为None时，调用父类方法为对象分配空间
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        # 返回内存地址
        return cls.instance

    def __init__(self):
        """
        初始化对象属性
        """
        # 判断是否执行过初始化操作，如果执行过初始化动作直接返回
        if MusicPlayer.init_flag:
            return
        print("播放器初始化")
        MusicPlayer.init_flag = True


# 创建对象
player = MusicPlayer()
player1 = MusicPlayer()
print(player)
print(player1)
