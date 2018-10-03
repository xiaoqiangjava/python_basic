#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 1. 定义两个变量python_score, c_score, 判断成绩，只要有一门成绩大于60分就合格
python_score = 67
c_score = 80

if python_score > 60 or c_score > 60:
    print("成绩合格")
else:
    print("成绩不合格")

# 2. 只有两门成绩都大于60分时才合格
if python_score > 60 and c_score > 60:
    print("成绩合格")
else:
    print("成绩不合格")

# 2. 定义一个布尔型变量is_employee, 如果不是本公司员工，禁止入内
# 在日常开发中，通常希望在不满足某个条件时执行代码块，可以使用not逻辑运算符，另外，
# 如果需要拼接复杂的逻辑运算，也会用到not逻辑运算符
is_employee = False
if not is_employee:
    print("非本公司员工请勿入内")
