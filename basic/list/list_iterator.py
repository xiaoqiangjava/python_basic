#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. 列表的迭代遍历：顺序的从列表中依次获取数据，每一次循环过程中，数据都会保存在name这个变量中，在
# 循环体内部可以访问到当前获取到的数据
name_list = ["xiaoqiang", "wenwen", "zhangsan", "lisi"]
for name in name_list:
    print("My name is %s" % name)

# 2. 应用场景：尽管python中的列表可以存储不同类型的数据，但在开发中更多的应用场景是：
# 列表存储相同类型的数据，通过迭代遍历，在循环体内部针对列表的每一项元素执行相同的操作
