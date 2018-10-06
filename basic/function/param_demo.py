#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. 缺省参数
# 定义函数时，可以指定缺省参数的默认值，当调用函数时，指定了缺省参数默认值的参数可以不用传递该参数
# 注意：定义函数时，带有默认值的缺省参数必须放在所有参数列表的末尾，否则会报错
# 当一个函数定义了多个缺省参数时，如果需要给某一个具体的参数指定具体的值需要在调用函数时指定缺省参数的参数名称


def print_info(name, title="学委", gender=True):
    """
    打印学生信息
    :param title: 职位
    :param name: 姓名
    :param gender: 性别
    :return: None
    """
    gender_str = "男生"
    if not gender:
        gender_str = "女生"
    print("【%s】%s 是 %s" % (title, name, gender_str))


print_info("xiaoqiang")
print_info("xiaowang", gender=False)

# 2. 多值参数：接收参数的个数是不确定的，这个时候就可以使用多值参数
# python中支持两种多值参数：
# 参数名前增加一个*的参数可以接收一个元组：*args
# 参数名前增加两个*的参数可以接收一个字典：**kwargs
# 其中真正的参数名是*或者**后面的部分，调用时不要带*调用变量


def demo(num, *nums, **person):
    print(num)
    print(nums)
    print(person)


demo(1, 2, 3, 4, 5)
demo(1, 2, 3, 4, 5, name="xiaoqiang", age=18, gender=True)
