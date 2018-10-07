#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 创建对象：类()做了两件事：
# 1. 调用__new__()为对象分配内存空间, 并返回分配空间的对象引用，传递给__init__()方法
# 2. 调用__init__()方法初始化对象属性


class MusicPlayer(object):
    """
    重写__new__()方法， 该方法必须要返回super().__new__(cls)
    """
    def __new__(cls, *args, **kwargs):
        """
        重写父类分配空间方法
        :param args:
        :param kwargs:
        :return: 对象的引用
        """
        # 创建对象时，__new__()方法会自动调用
        print("创建对象，分配空间")
        # 调用父类方法为对象分配空间
        instance = super().__new__(cls)
        # 返回内存地址
        return instance

    def __init__(self):
        """
        初始化对象属性
        """
        print("播放器初始化")


# 创建对象
player = MusicPlayer()
player1 = MusicPlayer()
print(player)
print(player1)
