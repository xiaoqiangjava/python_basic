#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. 完整for循环：else中的代码在没有用break退出的循环时执行, 如果循环是通过break跳出循环，则else代码块不执行
# 完整for循环通常使用在嵌套数据类型遍历时搜索功能，在未搜索到时统一提示代码在else中编写
info_list = ["xiaoqiang", "zhangsan", "lisi"]
find_name = "qianglong"
for name in info_list:
    print(name)
    if name == find_name:
        break
else:
    print("%s 不在列表中" % find_name)
