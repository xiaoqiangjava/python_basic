#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 递归函数(recursion)
# 1. 递归函数的特点：一个函数内部调用自己
# 2. 代码特点：函数内部的代码时相同的，只是针对不同的参数，处理的结果不同
# 当参数满足一定条件时函数不在执行，这个非常重要，时递归的出口，否则会形成死循环
# 3. 因为递归函数是针对不同的参数处理的结果不同，所以递归函数一定有参数
# 4. 递归在处理不确定的循环条件时特别有用，比如遍历文件夹中的目录


def recursion(num):
    """
    递归函数演示：在函数内部调用函数自己
    :param num:
    :return:
    """
    print(num)
    # 递归的出口跟while循环的循环条件一样重要
    if num < 0:
        return
    recursion(num - 1)
    # 调用结束后函数会一层一层的向上返回，执行下面的代码，所以先打印的是0
    print("完成 %d" % num)


recursion(5)
