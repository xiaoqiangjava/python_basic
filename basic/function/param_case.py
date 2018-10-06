#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. 对任意多个数字求和


def sum_nums(*args):
    """
    对任意多个数字求和
    :param args: 任意个数的参数
    :return: 求和的结果
    """
    sum_result = 0
    for num in args:
        sum_result += num
    return sum_result, args


result, param = sum_nums(1, 2, 4, 6, 45, 22)
print("%s的总和为：%d" % (param, result))


def demo(*args, **kwargs):
    """
    元组和字典拆包演示
    :param args: 元组参数
    :param kwargs: 字典参数
    :return:
    """
    print(args)
    print(kwargs)


# 2. 对元组和字典拆包
gl_tuple = (1, 2, 3)
gl_dict = {"name": "xiaoqiang", "age": 26}
# 如果直接将元组和字典传递给多值参数的函数，会将元组和字典都放入第一个多值参数中
# 如果需要对应的传递元组和字典，就需要对元组和字典进行拆包
# 手动拆包：
# demo(1, 2, 3, name="xiaoqiang", age=26)
# 可以在传入的参数前面加*实现自动拆包，一个*拆包成tuple, **两个*拆包成dict
demo(*gl_tuple, **gl_dict)

