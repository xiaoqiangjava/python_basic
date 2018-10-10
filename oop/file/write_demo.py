#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 打开文件的方式: "r"--只读模式; "w"--只写方式,如果文件不存在会创建文件, 是覆盖写; "a"--追加写, 不存在会创建文件


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

    def write(self):
        """
        写文件内容
        :return:
        """
        # 1. 打开文件
        file = open(self.name, "a", encoding="utf-8")
        # 2. 读取文件: 执行了read()方法后会将文件指针移动到文件末尾，再次执行方法不会读取到内容
        # read()方法默认以只读方式打开文件
        content = file.write("hello")
        print("%s 写入长度：\n%s" % (self.name, content))


if __name__ == "__main__":
    # 创建对象
    fillDemo = FileDemo("README")
    fillDemo.write()
