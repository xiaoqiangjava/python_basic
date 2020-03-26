#! /usr/bin/python
# -*- encoding: utf-8 -*-


# 数据结构检查练习
def is_valid(str):
    map = {'}': '{', ']': '[', ')': '('}
    stack = []
    for ch in str:
        if ch not in map:
            stack.append(ch)
        else:
            if not stack or map.get(ch) != stack.pop():
                return False

    return not stack
