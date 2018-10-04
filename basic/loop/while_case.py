#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. 累计求和：计算0-100之间所有数字的累加求和
i = 0
sum = 0
while i <= 100:
    sum += i
    print("当前计数器的值为：%d" % i)
    i += 1
print("0-100的累计和为：%d" % sum)
print("=" * 10)

# 2. 偶数求和：0-100之间所有偶数求和
# 方式一：
i = 0
sum = 0
while i <= 100:
    if i % 2 == 0:
        print("当前计数器的值为：%d" % i)
        sum += i
    i += 1
print("0-100之间偶数求和结果为：%d" % sum)
print("=" * 10)

# 方式二：
i = 0
sum = 0
while i <= 100:
    sum += i
    print("当前计数器的值为：%d" % i)
    i += 2
print("0-100之间所有偶数的和为：%d" % sum)
