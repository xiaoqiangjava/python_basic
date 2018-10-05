#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. python 中的非数字类型有一些公共的方法： len(), del(), max(), min(), +, *, in, not in

# 2. 非数字型数据类型的公共函数：str, tuple, list, dict
# len() 统计容器中元素个数
# del() 删除元素或者变量
# max() 获取容器中最大的值，如果是dict，则只针对key比较
# min() 获取容器中最小的值，如果是dict，则只针对key比较

# 3. 切片：支持list, tuple, str

# 4. *(重复): 支持str, list, tuple
print((1, 2) * 3)

# 5. +(拼接): 支持str, list, tuple. 拼接后生成一个新的元组
# +跟list的extexd()方法相识，区别在于extend()是修改原来的列表，而+运算会生成新的列表
print((1, 2) + (3, 4))
print([1, 2] + [3, 4])
tuple_info = (3, 4)

# 6. in 和 not in：支持str, list, tuple, dict(key)
# in 和 not in 是成员运算符，in表示包含，not in表示不包含, 判断dict时判断key
print(2 in [2, 5])
print(3 not in (3, 5))
print("name" in {"name": "xiaoqiang"})
