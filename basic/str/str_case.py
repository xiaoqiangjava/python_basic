#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 字符串常用方法
# 1. 通过索引取值
str3 = "hello python"
print(str3[1])
# 截取字符串
print("截取hello: ", str3[0:5])
print("截取python: ", str3[6:])

# 2. 统计
# 2.1 统计字符串的长度
print("str3字符串的长度：", len(str3))

# 2.2 统计字符在字符串中出现的次数,如果指定的字符串不存在,则次数是0
print("str3中o字符出现的次数：", str3.count("o"))
print("str3中xq出现的次数：", str3.count("xq"))

# 3. 索引: str.index(char)方法可以获取指定字符在字符串中第一次出现的索引位置
# 当指定的子字符串不存在时报错：ValueError： substring not found
print("o第一次出现的索引：", str3.index("o"))
# print("str3中xq出现的索引为：", str3.index("xq"))
