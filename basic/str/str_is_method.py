#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. 判断类型
# 1.1 判断空白字符: 如果只包含空白字符，包括转义字符\t\n\r则返回True
space_str = " \t\n\r"
print(space_str.isspace())

# 1.2 判断字符串是否只包含字母
num_str = "adRBFE"
print("=" * 20)
print(num_str.isalpha())

# 1.3 判断字符串是否只包含字母和数字: isalnum是isalphanum的缩写
num_str = "seKIH23"
print("=" * 20)
print(num_str.isalnum())

# 1.4 判断字符串是否只包含数字: 三个方法都不能判断小数， isdecimal, isdigit, isnumeric判断的范围越来越大
# isdecimal只能判断纯数字，常用，isdigit还可以判断unicode数字，isnumeric还可以判断中文的数字一
num_str = "13434"
print("=" * 20)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())

# 1.5 判断字符串中的字母是否都是小写字母
lower_str = "kdfAd23"
print("=" * 20)
print(lower_str.islower())

# 1.6 判断字符串中的字母是否都是大写字母
upper_str = "ADBV"
print("=" * 20)
print(upper_str.isupper())

# 1.7 判断是否是正确的标识符: 表示符不能以数字开头
id_str = "23DDK"
print("=" * 20)
print(id_str.isidentifier())

