#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. 元组的遍历：使用迭代遍历。在python中，for ... in ...：循环可以遍历所有的非数字型类型的元素，
# 包括str, list, tuple, dict
tuple_info = ("xiaoqiang", 25, 170)
for my_info in tuple_info:
    print(my_info)

# 2. 元组中通常保存的数据类型是不同的，使用迭代遍历时无法对变量执行相同的操作，所以元组很少用来迭代遍历
# 2.1 元组的应用
# 2.1.1 格式化字符串时% ()就是一个tuple
tuple_info = ("xiaoqiang", 25, 1.75)
print("我是 %s, 今年 %d岁, 身高%.2f" % tuple_info)
info_str = "我是 %s, 今年 %d岁, 身高%.2f" % tuple_info
print(info_str)

# 2.1.2 可以作为函数的参数或者返回值，当以元组为参数时，可以给函数传递任意多个参数，返回tuple类型的数据可以让函数
# 返回多个返回值

# 2.1.3 将tuple转换成list
info_list = ["xiaoqiang", "zhangsan", "wenwen"]
list_2_tuple = tuple(info_list)
print(type(info_list))
print(type(list_2_tuple))

# 2.1.4 将list转换成tuple
tuple_2_list = list(tuple_info)
print(type(tuple_2_list))


