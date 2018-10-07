#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 方法和属性综合案例：
# 定义一个Game类，包含一个top_score记录历史最高分，定义一个实例属性player_name记录玩姓名
# 静态方法show_help显示帮助信息（既不访问类属性，也不访问实例属性）
# 类方法show_top_score显示历史最高分（访问类属性）
# 实例方法start_play开始当前玩家的游戏


class Game(object):
    """
    游戏类
    """
    top_score = 0

    @staticmethod
    def show_help():
        """
        静态方法，显示游戏帮助信息
        :return:
        """
        print("这里是游戏帮助信息")

    @classmethod
    def show_top_score(cls):
        """
        这是一个类方法，显示类属性历史最高分
        :return:
        """
        print("历史最高分：%d" % cls.top_score)

    def __init__(self, name):
        """
        初始化对象的属性
        :param name: 玩家名称
        """
        self.player_name = name

    def start_play(self):
        """
        当前玩家开始游戏
        :return:
        """
        print("%s 开始游戏啦。。。" % self.player_name)


# 显示帮助信息
Game.show_help()
Game.show_top_score()
game = Game("xiaoqiang")
game.start_play()
