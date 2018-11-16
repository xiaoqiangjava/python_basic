#! /usr/bin/python
# -*- encoding: utf-8 -*-
import unittest
import debug.unittest.unittest as test


class DictTest(unittest.TestCase):
    """
    单元测试类需要继承unittest模块中的TestCase, 继承之后类中所有test开头的方法都是test方法, 不以test开头的
    方法不被认为是测试方法, 测试的时候不会被执行
    """
    def test_init(self):
        d = test.Dict(name="Jack", age=25)
        self.assertEqual(d.name, "Jack")
        self.assertEqual(d.age, 25)

    def test_getattr(self):
        d = test.Dict(name="Jack", age=25)
        self.assertEqual(d.__getattr__("name"), "Jack")
        self.assertTrue("phone" in d)

    def test_errorkey(self):
        d = test.Dict()
        with self.assertRaises(KeyError):
            d['key']


if __name__ == 'main':
    # 通过unittest的main方法启动单元测试
    unittest.main
