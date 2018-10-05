#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. 元组的定义: 元组使用（）定义，元组的元素不能修改
tuple_info = ("xiaoqiang", 25, 170, "xiaoqiang")
print("tuple_info的第一个元素：", tuple_info[0])

# 2. 定义一个空元组
empty_tuple = ()
print(type(empty_tuple))

# 3. 定义一个只包含一个元素的元组: 定义单元素元组时，需要在元素后面加上分隔符逗号，否则python解释器会忽略掉括号
# 把元组的元素类型当做定义的变量的类型来处理
single_tuple = (5,)
print(type(single_tuple))

# 4. 元组的内部方法
# 4.1 tuple.index()方法可以获取已知元素在元组中的索引
print("xiaoqiang在元组中的索引：", tuple_info.index("xiaoqiang"))
# 4.2 tuple.count()方法统计已知元素在元组中出现的次数
print("xiaoqiang在元组中出现的次数：", tuple_info.count("xiaoqiang"))
# 4.2 统计元组中包含的元素个数
print("tuple_info元组中包含的元素个数：", len(tuple_info))
