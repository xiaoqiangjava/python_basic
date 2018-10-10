#! /usr/bin/python
# -*- encoding: utf-8 -*-

# python 对文件的操作包括三个步骤：1.打开文件；2.读写文件；3.关闭文件
# 如果忘记关闭文件会造成系统资源的消耗和后续对文件的操作
# 注意：Linux下文件名区分大小写


class FileDemo(object):
    """
    文件操作演练
    """
    def __init__(self, name):
        """
        初始化对象的属性
        :param name: 文件名称
        """
        self.name = name

    def read(self):
        """
        读取文件内容
        :return:
        """
        file = None
        try:
            # 1. 打开文件
            file = open(self.name, encoding="utf-8")
            # 2. 读取文件: 执行了read()方法后会将文件指针移动到文件末尾，再次执行方法不会读取到内容
            # read()方法默认以只读方式打开文件
            content = file.read()
            print("%s 文件内容：\n%s" % (self.name, content))
        except FileNotFoundError as result:
            print("%s 文件不存在" % self.name)
            print(result)
        finally:
            # 在finally中关闭文件
            if file is not None:
                file.close()


if __name__ == "__main__":
    # 创建对象
    fillDemo = FileDemo("__init__.py")
    fillDemo.read()
