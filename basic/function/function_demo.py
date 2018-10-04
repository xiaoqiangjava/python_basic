#! /usr/bin/python
# -*- encoding: utf-8 -*-


def say_hello():
    """
    1. 函数的定义和使用, def是define的缩写，say_hello是函数名称
    PEP 8 中建议在方法和类的定义前后加两个空行
    函数的说明文档通过三个"来引出，可以使用快捷键F2查看方法说明
    :return:
    """
    print("hello")


# 调用函数，python中定义的函数不主动调用是不会运行的，可以通过函数名()的方式调用一个函数
say_hello()


def sum_2_num(num1, num2):
    """
    两个数求和
    :param num1: 第一个加数
    :param num2: 第二个加数
    :return: result
    """
    result = num1 + num2
    print("%d + %d = %d" % (num1, num2, result))
    return result


# 调用两个数求和函数
# 函数的参数：
# 形参：定义函数时，小括号中的参数，是用来接收参数用的，在函数内部作为变量使用
# 实参：调用函数时，小括号中的参数，是用来将数据传递到函数内部用的
sum_result = sum_2_num(15, 34)
print("计算结果为: %d" % sum_result)

