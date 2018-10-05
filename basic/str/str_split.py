#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. 字符串的拆分和链接
# 1.1 string.partition(str) 将字符串分隔成一个三元素的元组(str前面, str, str后面)tuple
char_str = "ABCECBA"
print(char_str.partition("E"))
print(type(char_str.partition("E")))

# 1.2 string.split(str) 使用指定的分隔符将一个字符串分隔成一个字符串列表list
split_str = "hi, my name is xiaoqiang"
str_list = split_str.split(",")
print(str_list)
print(type(str_list))

# 1.3 str.join(list) 字符串的拼接: 将序列中的所有元素以str作为分隔合并成一个字符串
join_str = " ".join(str_list)
print(join_str)
