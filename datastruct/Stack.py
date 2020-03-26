#! /usr/bin/python
# -*- encoding: utf-8 -*-


def is_valid(str):
    """
    判断括号字符串是否匹配
    :param str:
    :return:
    """
    paren_map = {'{': '}', '[': ']', '(': ')'}
    stack = []
    for ch in str:
        if ch not in paren_map:
            stack.append(ch)
        else:
            if not stack or paren_map[ch] != stack.pop():
                return False

    return not stack


class MyStack:
    """
    通过队列实现栈的功能
    """
    def __init__(self):
        self.queue = []
        self.temp = []
        # python中函数名称和变量名称不能重名
        self.top_e = -1

    def push(self, x):
        """
        :type x: int
        """
        self.queue.append(x)
        self.top_e = x

    def pop(self):
        res = self.top_e
        while len(self.queue) > 1:
            self.top_e = self.queue.pop(0)
            self.temp.append(self.top_e)

        self.queue.pop(0)
        tmp = self.queue
        self.queue = self.temp
        self.temp = tmp

        return res

    def empty(self):
        return not self.queue

    def top(self):
        return self.top_e


stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack.empty())
print(stack.top())
