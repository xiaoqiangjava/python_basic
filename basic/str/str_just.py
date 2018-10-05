#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. 文本对齐
# 1.1 str.center(width, fillchar)方法可以让文本居中对齐
poem = ["登黄鹤楼", "王之涣", "白日依山尽", "黄河入海流", "欲穷千里目", "更上一层楼"]
for poem_str in poem:
    print("|%s|" % poem_str.center(20, "　"))

# 1.2 str.ljust()使文本左对齐
for poem_str in poem:
    print("|%s|" % poem_str.ljust(20, "　"))

# 1.2 str.rjust()使文本右对齐
for poem_str in poem:
    print("|%s|" % poem_str.rjust(20, "　"))
