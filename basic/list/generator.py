#! /usr/bin/python
# -*- encoding: UTF-8 -*-


# 生成器: 在python中一遍循环一遍计算的元素值的机制叫做生成器: generator
# 将列表生成式中的[]修改为(), 就创建了一个generator, generator有next方法可以获取下一个元素
# 通常使用for循环遍历generator, 因为generator是一个iterator
generator = (x * x for x in range(5))
for e in generator:
    print(e)


# 如果一个函数定义中包含yield, 那么这个函数不再是一个普通函数, 而是一个generator. generator函数的调用
# 实际返回的是一个generator对象
def odd():
    yield 1
    yield 2
    yield 3


# 调用generator函数返回的是一个generator对象
o = odd()
next(o)
next(o)
next(o)
