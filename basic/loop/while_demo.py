#! /usr/bin/python
# -*- encoding: utf-8 -*-

# while循环语句: 打印5遍hello world
# 在循环体内部一定要修改计数器的数值，否则就会形成死循环
i = 1
while i <= 5:
    print("hello world")
    print("当前条件的值为：%d" % i)
    i = i + 1

# python中的赋值运算符
# = 简单的赋值运算符，c = a + b 将a + b的结果赋值给c
# += 加法赋值运算符，c += a相当于c = c + a
# -= 减法赋值运算符，c -= a相当于c = c - a
# *= 乘法赋值运算符，c *= a相当于c = c * a
# /= 除法赋值运算符，c /= a相当于c = c / a
# //= 取整赋值运算符，c //= a相当于c = c // a
# %= 取模（余数）赋值运算符，c %= a相当于c = c % a
# **= 幂赋值运算符，c -= a相当于c = c - a

# 根据苹果的单价和重量计算苹果的总价
price = 4.68
wight = 12
total_price = price * wight
print("苹果的总价为: %.2f" % total_price)
print(total_price // wight)
