#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 主动抛出异常:raise Exception(*args)


def input_pwd():
    # 提示用户输入密码
    password = input("请输入密码：")
    # 判断密码长度，>=8, 打印密码
    if len(password) >= 8:
        print(password)
    else:
        # 小于8，抛出raise异常
        raise Exception("密码的长度必须最少为8位")


try:
    input_pwd()
except Exception as result:
    print(result)
