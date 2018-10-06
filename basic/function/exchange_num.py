#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 两个数字的交换
a = 100
b = 50

# 解法一
c = a
a = b
b = c
print(a)
print(b)
print("-" * 50)

# 解法二
a = a + b
b = a - b
a = a - b
print(a)
print(b)
print("-" * 50)

# 解法三：python专用，利用元组
# a, b = (b, a)当一个函数的返回值是元组时，可以省略()，所以可以简写成a, b = b, a
# 注意：等号右边是一个元组
a, b = b, a
print(a)
print(b)
