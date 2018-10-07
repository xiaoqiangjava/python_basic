#! /usr/bin/python
# -*- encoding: utf-8 -*-

# python中支持多继承，这根Java的区别很大，Java只支撑单继承
# class A(B, C): A类继承B和C两个类
# 在开发中如果出现两个父类中出现了同名的方法，应该尽量避免出现多继承
# 注意：如果多继承时两个父类中存在两个同名的方法，子类会调用哪个方法？可以通过修改类继承的顺序改变调用顺序
# python针对类提供了一个内置属性__mro__,可以查看方法搜索顺序
# MRO Method Resolution Order即方法搜索顺序


class A:
    def demo(self):
        print("A---demo方法")

    def test(self):
        print("A---test方法")


class B:
    def demo(self):
        print("B---demo方法")

    def test(self):
        print("B---test方法")


class C(A, B):
    pass


# 创建c对象
c = C()
c.test()
c.demo()
print(C.__mro__)
