#! /usr/bin/python
# -*- encoding: utf-8 -*-


# 分治算法：将一个问题分解为多个子问题，然后将子问题的解合并为当前问题的解
def myPow(x, n):
    """
    求解x的n次方
    LeetCode: 50
    :type x: float
    :type n: int
    :rtype: float
    """
    if not n:
        return 1.0
    if n < 0:
        return 1 / myPow(x, -n)
    if n % 2 != 0:
        return x * myPow(x, n - 1)
    return myPow(x * x, n // 2)
