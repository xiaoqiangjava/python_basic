#! /usr/bin/python
# -*- encoding：utf-8 -*-

# 1. 函数的嵌套


def print_line(char, times):
    """
    打印单行分隔线, 任意字符任意次数的分隔线
    :return:
    """
    print(char * times)


def print_lines(counter, char, times):
    """
    打印多行分隔线，打印的行数通过参数传递
    :param counter: 需要打印分隔线的行数
    :param char: 需要打印分隔线的字符
    :param times: 分隔线的重复次数
    :return:
    """
    i = 0
    while i < counter:
        print_line(char, times)
        i += 1


# 调用打印单行分隔线函数
print_line("-", 50)

# 调用打印多行分隔线函数
print_lines(5, "*", 50)
