#! /usr/bin/python
# -*- encoding: utf-8 -*-

# readLine()一次读取一行内容,适合读取大文件, 减小内存压力


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

    def read_line(self):
        """
        读取文件内容
        :return:
        """
        file = None
        try:
            # 1. 打开文件
            file = open(self.name, encoding="utf-8")
            while True:
                # 2. 读取文件: 执行了read()方法后会将文件指针移动到文件末尾，再次执行方法不会读取到内容
                # read()方法默认以只读方式打开文件
                content = file.readline()
                if not content:
                    break
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
    fillDemo.read_line()
