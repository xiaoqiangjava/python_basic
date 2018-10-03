#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. 女友节日：情人节--》买玫瑰花，看电影；平安夜--》买苹果，吃大餐；生日--》买蛋糕
holiday_name = input("请输入节日名称：")
if holiday_name == "情人节":
    print("买玫瑰，看电影")
elif holiday_name == "平安夜":
    print("买苹果，吃大餐")
elif holiday_name == "生日":
    print("买蛋糕，唱生日歌")
else:
    print("全是女友的节日啊。。。")

# 2. 定义一个布尔变量has_ticket, 表示是否有车票，一个整型变量knife_length, 表示刀的长度
# 需求：火车站进站时需要检票，有票的情况下不能带超过20cm的刀进入
has_ticket = True
knife_length = 30
if has_ticket:
    print("车票检验通过，准备开始安检")
    if knife_length > 20:
        print("不能携带超过 20 cm的刀进入车站内，你携带的道具长度为：%d cm" % knife_length)
    else:
        print("安检通过，请携带好随身物品入内")
else:
    print("请您先购买车票")
