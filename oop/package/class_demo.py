#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 类的定义：class 类名： 其中类名遵循大驼峰命名，即首字母大写的驼峰命名


class Cat:
    """
    这是一个猫类
    """

    def eat(self):
        # 哪个对象调用方法，self就是对调用方法对象的引用，所以在方法内部可以可以使用self.调用对象的方法和属性
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("%s爱喝水" % self.name)


# 创建猫对象: 类名()
tom = Cat()

# 使用同一类创建的不同对象，该对象在内存中的地址不同，即两个对象是不同的对象
# python中给一个对象添加属性：.属性名 = 属性值，不推荐使用
tom.name = "Tom"

tom.eat()
tom.drink()
print(dir(tom))
print(tom.__doc__)
print(tom)
# %x可以打印16进制的值
print("%x" % id(tom))

# 再创建一个猫对象
lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)
