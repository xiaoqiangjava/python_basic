#! /usr/bin/python
# -*- encoding: utf-8 -*-
import random

# 1. 综合案例：石头剪刀布, 玩家输入自己出的拳，石头、剪刀、布, 电脑随机出拳，比较输赢
# 用户通过控制台输入要出的拳
player = int(input("请输入您要出的拳（1：石头，2：剪刀，3：布）："))

# 电脑随机出拳: random模块中的randint(a, b) 可以生成一个随机数，这个随机数的取值范围：a <= int <= b
# 即生成的随机数包含开始和结束的值，并且传入的参数b>=a
computer = random.randint(1, 3)
print("玩家出的拳：%d, 电脑出的拳：%d" % (player, computer))

# 判断胜负
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("恭喜玩家取得胜利")
elif player == computer:
    print("平局, 再来一局")
else:
    print("电脑获胜")

