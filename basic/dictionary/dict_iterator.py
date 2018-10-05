#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. 字典的遍历: 直接遍历拿到的是字典的key
xq_info = {"name": "xiaoqiang", "age": 26, "gender": True}
for key in xq_info:
    print("%s : %s" % (key, xq_info.get(key)))

# 2. 遍历所有的key
for key in xq_info.keys():
    print("%s" % key)

# 3. 遍历所有的value
for value in xq_info.values():
    print(value)

# 4. 遍历item
for (key, value) in xq_info.items():
    print("%s : %s" % (key, value))
