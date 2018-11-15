#! /usr/bin/python
# -*- encoding: UTF-8 -*-
import os


# 列表生成式(List Comprehensions)是python内置的非常简单且强大的用来创建list的生成式
# 写列表生成式时, 要把生成的元素放到前面, 后面跟for循环
list_num = [x * x for x in range(1,  11)]
print(list_num)

# 可以使用两层for循环生成全排列
list_char = [m + n for m in 'ABCD' for n in '1234']
print(list_char)

# 使用列表生成式可以轻松的列出当前目录下面的文件和目录
list_dir = [d for d in os.listdir(".")]
print(list_dir)

# 列表生成式还可以在for循环后面跟if表达式过滤需要生成的元素
list_num = [x * x for x in range(5) if x % 2 == 0]
print(list_num)

# 列表生成式还可以使用两个变量来生成list
d = {"name": "Jack", "age": 23}
list_key = [k + '=' + str(v) for k, v in d.items()]
print(list_key)
