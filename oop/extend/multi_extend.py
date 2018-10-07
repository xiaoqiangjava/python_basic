#! /usr/bin/python
# -*- encoding: utf-8 -*-

# python中支持多继承，这根Java的区别很大，Java只支撑单继承
# class A(B, C): A类继承B和C两个类
# 注意：如果多继承时两个父类中存在两个同名的方法，


class A:
    def test(self):
        print("A---test方法")


class B:
    def demo(self):
        print("B---demo方法")


class C(A, B):
    pass


# 创建c对象
c = C()
c.test()
c.demo()
