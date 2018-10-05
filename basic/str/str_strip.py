#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. 去除字符串的空白字符
# 1.1 去除字符串两边的空白字符: 可以指定去除的字符
trip_str = "    hello python    "
print(trip_str.strip())
trip_str = "---hello python----"
print(trip_str.strip("-"))

# 1.2 去除字符串左边的字符
print(trip_str.lstrip("-"))

# 1.3 去除字符串右边的字符
print(trip_str.rstrip("-"))
