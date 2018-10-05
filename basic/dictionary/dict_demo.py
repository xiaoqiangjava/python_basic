#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. 字典的定义: 字典是一个无序的数据集合, 字典的键是不能重复的, python中的字典key和value都可以为None
xq_info = {"name": "xiaoqiang", "age": 25, "gender": True, "height": 1.70, "weight": 61.40, None: None}
print(xq_info)

# 2. dict的基本增删改查操作
# 2.1 取值：在取值的时候如果指定的key不存在会报错：keyError
xq_name = xq_info["name"]
print("xq_info中的名字：", xq_name)
xq_name = xq_info.get("name")
print("xq_info中的名字：", xq_name)

# 2.2 增加/修改: 如果key不存在，在字典中增加key-value, 如果key存在，则修改该key对应的value
xq_info["girl"] = "wenwen"
print(xq_info)
xq_info["age"] = 26
print(xq_info)

# 2.3 删除: pop可以删除指定的key，如果指定的key不存在，则报错： keyError
xq_info.pop("girl")
print(xq_info)

# 2.4 统计：len()函数可以统计字典中键值对的数量
print("xq_info中键值对中的数量：", len(xq_info))

# 2.5 合并字典: dict.update(dict)方法可以合并两个dict，当字典中已经存在新的key时，则更新该key对应的vaule
temp_info = {"girl": "wenwen"}
xq_info.update(temp_info)
print(xq_info)

# 2.6 清空字典：dict.clear()
xq_info.clear()
print(xq_info)

