#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. 字符串切片：str[start:end:step], 区间属于左闭右开型
str_str = "hello python"

# 1.1 从头开始截取，start可以省略，：不能省略
print("切区hello: ", str_str[:5])

# 1.2 截取到末尾，end可以省略，：不能省略
print("截取python: ", str_str[6:])

# 1.3 倒序截取
print("截取python: ", str_str[-6:])

# 1.4 每隔两个字符截取
num_str = "0123456789"
print("偶数：", num_str[::2])

# 1.5 字符串逆序: 当指定的step为-1时，将从右向左切
print(num_str[::-1])

# 1.6 截取中间位置: 包含start，不包含end
print(num_str[3:7])
