#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. python中的数据类型分为数字类型和非数字类型，其中数字类型有int, float, bool(0表示True, 1表示False), complex(复数型）
#    非数字类型: str(字符串), list(列表), tuple元组, dict(字典)
# 2. 列表的定义, list的索引从零开始
name_list = ["xiaoqiang", "wenwen", "baoer", "xiaoqiang"]
print("name_list: ", name_list)

# 3. 列表中的内置函数
# 3.1 取值和取索引
# 3.1.1 从列表中取值时，如果索引超出范围时报错：IndexError: list index out of range
print("name_list的第一个元素：", name_list[0])
print("name_list的第一个元素：", name_list.__getitem__(0))
# 使用index()获取元素的索引时，如果传递的数据不在列表中，报错：ValueError: '' is not in list
print("xiaoqiang在name_list中的索引位置：", name_list.index("xiaoqiang"))

# 3.2 统计
# 3.2.1 list.__len__()函数可以返回列表的大小
print("name_list的长度：", name_list.__len__())
# 3.2.2 len(list)该函数可以返回列表的大小，使用__len__()函数时，内部就是使用该函数返回的列表的大小
print("name_list的长度：", len(name_list))
# 3.2.3 list.count(数据) 返回数据在list中出现的次数
print("xiaoqiang在列表中出现的次数为：", name_list.count("xiaoqiang"))

# 3.3 修改
# 3.3.1 修改指定位置的数据, 当索引超出范围时报错：IndexError: list assignment index out of range
name_list[2] = "baobao"
print("修改指定位置的值后：", name_list)

# 3.4 新增数据
# 3.4.1 list.append()方法可以向列表中追加数据
name_list.append("zhangsan")
# 3.4.2 list.insert(index, object)可以在列表指定索引位置插入数据
name_list.insert(1, "美女")
print("新增数据后的name_list: ", name_list)
# 3.4.3 list.extend(list)方法可以将其他列表中的内容追加到新的列表中
temp_list = ["孙悟空", "猪八戒", "沙师弟"]
name_list.extend(temp_list)
print("extend方法追加之后的name_list: ", name_list)

# 3.5 删除数据
# 3.5.1 list.remove(数据)方法可以从数组中删除指定元素, 如果数据出多次, 会删除第一次出现的数据
name_list.remove("美女")
print("删除美女后的name_list: ", name_list)
# 3.5.2 list.pop([index])默认删除最后一个元素，可以指定index删除指定的元素
name_list.pop()
name_list.pop(3)
print("使用pop删除最后一个和指定元素后的name_list: ", name_list)
# 3.5.3 list.clear() 方法可以清空list中的所有元素
name_list.clear()
print("清空之后的name_list: ", name_list)
# 3.5.4 del list[index] 将一个元素从内存中删除，del关键字可以删除任意类型的变量
# 当使用del将变量从内存中删除以后，后面的代码就不能使用该变量了
del name_list

# 3. 元组的定义
name_tuple = (12, 23)
print("name_tuple: ", name_tuple)
print("name_tuple的第一个元素：", name_tuple[0])
print("name_tuple的长度：", name_tuple.__len__())

# 4. 字典的定义
name_dic = {"name": "xiaoqiang"}
print("name_dict中name的值为：", name_dic["name"])
print("name_dict的长度为：", name_dic.__len__())
