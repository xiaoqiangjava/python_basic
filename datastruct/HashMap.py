#! /usr/bin/python
# -*- encoding: utf-8 -*-


# 判断字符串是否是异位词：LeetCode 242
def is_anagram(s, t):
    dict1, dict2 = {}, {}
    for ch in s:
        dict1[ch] = dict1.get(ch, 0) + 1
    for ch in t:
        dict2[ch] = dict2.get(ch, 0) + 1

    # 在python中==判断两个对象的值是否相等，is是判断是否是同一个对象
    return dict2 == dict1


# tow sum, LeetCode 1
def tow_sum(nums, target):
    """
    查找集合中是否存在两个数的和为target的值的下标
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    map_nums = dict()
    for i, num in enumerate(nums):
        if target - num in map_nums:
            return [i, map_nums[target - num]]

        map_nums[num] = i
    return []
