#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. 对列表进行排序
num_list = [1, 4, 6, 9, 5]
name_list = ["xiaoqiang", "zhangsan", "lisi"]
num_list.sort()
name_list.sort()
print("升序排序后的num_list: ", num_list)
print("升序排序后的name_list: ", name_list)
num_list.sort(reverse=True)
name_list.sort(reverse=True)
print("降序排列后的num_list: ", num_list)
print("降序排列后的name_list: ", name_list)

# 2. 将类表反转（逆序）
name_list = ["zhangsan", "lisi", "xiaoqiang"]
name_list.reverse()
print("反转后的name_list：", name_list)

# 3. 函数和方法的区别
# 函数封装了特定的功能，可以直接调用，方法和函数类似，但方法是通过对象来调用的
# 函数名称需要记住的，而对象的方法可以使用快捷键查看方法的说明
