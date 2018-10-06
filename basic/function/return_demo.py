#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 当一个函数返回多个数据时，可以使用元组，元组中可以包含多个数据
# 当一个函数的返回值时一个元组时，元祖的()可以省略


def measure():
    """
    测量温度和是不
    :return:
    """
    print("测量开始。。。")
    temp = 39
    wetness = 60
    # return (temp, wetness)
    return temp, wetness


# 函数的返回结果是元组
result = measure()
print(result)
print(type(result))

# 当函数的返回值是一个元组时，同时希望单独处理元组中的元素，可以使用多个变量，一次接收函数的返回结果
# 注意：使用多个变量接收函数返回结果时，变量的个数应该和元组中元素的个数保持一致，否则程序会报错
gl_temp, gl_wetness = measure()
print("函数返回的温度：%d" % gl_temp)
print("函数返回的湿度: %d" % gl_wetness)

