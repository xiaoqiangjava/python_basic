#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 捕获异常：python中的异常同样具有传递性，可以在主程序中捕获异常


def demo1():
    try:
        num = int(input("请输入一个整数："))
        print(num)
    except:
        print("请输入正确的整数")


def demo2():
    try:
        num = int(input("请输入一个整数："))
        print(num)
        # 使用8除以用户输入的整数并输出
        result = 8 / num
        print(result)
    except ValueError as e:
        print(e)
        print("请输入正确的整数")
    except ZeroDivisionError:
        print("请输入非零数字")
    except Exception as result:
        print("这里捕获未知错误：%s" % result)
    else:
        print("程序正确执行，没有异常时执行的代码")
    finally:
        print("程序不管是否有异常，都会执行的代码")


demo1()
demo2()
print("-" * 50)
