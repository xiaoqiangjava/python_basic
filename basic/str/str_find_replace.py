#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. 字符串的查找和替换
# 1.1 startswith(str)判断是否已str开始
start_str = "hello world world"
print(start_str.startswith("hello"))

# 1.2 判断字符串已str结尾
print("=" * 20)
print(start_str.endswith("ld"))

# 1.3 查找字符串: find方法和index方法类似可以返回字符在字符串中的索引，当字符不存在时find方法返回-1，index会报错
print("=" * 20)
print(start_str.find("00"))
print(start_str.index("h"))

# 1.4 字符串的替换：不会修改原来字符的内容，会返回一个新的字符串, 当旧字符串不存在时不会替换，默认替换所有出现的字符
print("=" * 20)
print(start_str.replace("world", "python"))
print(start_str)

