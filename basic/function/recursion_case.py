#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 递归案例：传入一个参数n，计算1...n的累计求和


def sum_nums(num):
    """
    传入一个参数n，计算1...n的累计求和
    :param num: 传入的参数
    :return: 累计求和的结果
    """
    # 递归出口
    if num == 1:
        return 1
    # 递归调用自己实现累计求和
    temp = sum_nums(num - 1)
    return temp + num


result = sum_nums(5)
print("1..100的和为：%d" % result)
