#! /usr/bin/python
# -*- encoding: utf-8 -*-
# 用一种方法，最好是只有一种方法来做一件事情
str1 = "This is str test"
print(str1)
name = "xiaoqiang"
str2 = "My name is xiaoqiang"
age = 25

'''
    格式化符号：s表示后面的值是任意字符串，使用str()函数转换，s表示整数，f表示浮点数
    %[(name)][flags][width][.precision]typecode
    (name)--字典中的键
    flags--可以使用-+0三个标志：-表示左对齐，默认使用右对齐，+表示包含数字符号，正数也会带+，0表示一个0填充 
    width--一个指定最小宽度的数字
    .precision--指定要打印一个字符串中的最大字符串个数，浮点数中小数点后的位数，或者整数的最小位数
'''


def str_format():
    _str2 = "My name is %s" % name
    print("格式化字符串：" + _str2)
    _age = 25
    _str2 = "My name is %s, age is %d" % (name, _age)
    print("格式化字符串：" + _str2)
    f1 = 23.22
    print("This float is %0.3f" % f1)
    print("This float is %10.3f" % f1)
    d = {"name": "xiaoqiang", "age": 25}
    print("My name is %(name)s, age is %(age)d" % d)


# 获取一个对象的类型type()
def get_type():
    print("str2的类型：")
    print(type(str2))
    print("age的类型：")
    print(type(age))
    print("使用str转换后的类型：")
    print(type(str(age)))
    pass


# 字符串截取
def sub_str():
    print("str2中的第一个字符：" + str2[0])
    print("str2中的最后一个字符：" + str2[-1])
    print("截取str2中的2-5个字符：" + str2[1:5])
    print("截取str2中2-末尾的字符：" + str2[1:])
    print("截取str2时设置步长：" + str2[1::2])
    pass


# 所有方法入口
def __main__():
    _name = input("请输入需要执行的方法：str_format|get_type|sub_str=>")
    print("name的值：", _name)
    if _name == "str_format":
        str_format()
    elif _name == "get_type":
        get_type()
    elif _name == "sub_str":
        sub_str()
    else:
        print("请传入正确的方法名！")
        return
    pass


# 入口方法调用
if __name__ == "__main__":
    __main__()
