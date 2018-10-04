#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. break: 在循环体内部，当某一个条件满足时，退出循环，不再执行后面重复的代码
i = 0
while i < 10:
    print("当前计数器的值为：%d" % i)
    if i == 5:
        break
    i += 1
print("循环结束时计数器的值为：%d" % i)

# 2. continue: 在循环体内部，当某一个条件不满足时，不执行后面重复代码块
i = 0
while i < 10:
    print("if前计数器的值为：%d" % i)
    if i == 5:
        i += 1
        # 注意：在循环中使用continue关键字时，需要确认循环的计数器是否修改，否则会形成死循环
        continue
    print("if后计数器的值为：%d" % i)
    i += 1
print("循环体结束时计数器的值为：%d" % i)
