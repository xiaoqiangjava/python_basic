#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. 打印5行*，每一行的*的数量递增
row = 1
while row <= 5:
    print("*" * row)
    row += 1
print("==" * 10)

# 2. 使用循环嵌套，完成*的打印
# 分析：内层循环的循环次数与行号相同，外层循环控制行，内层循环控制列
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    # 每一行*输出完成之后输出一个换行符
    print("")
    row += 1

# 3. 使用嵌套循环实现九九乘法表
# 为了保证乘法表垂直方向对齐，可以使用转义字符，\t表示一个制表符，可以让代码垂直方向对齐，也可以使用%-2d实现格式化
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d * %d = %d" % (j, i, (j * i)), end="\t")
        j += 1
    i += 1
    print("")
