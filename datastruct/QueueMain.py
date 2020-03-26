#! /usr/bin/python
# -*- encoding: utf-8 -*-


# 滑动窗口，找出array中的最大值, LeetCode: 239
def max_sliding_window(nums, k):
    # 校验参数
    if not nums:
        return []

    window, res = [], []
    for idx, num in enumerate(nums):
        # window[0] <= idx - k保证窗口的大小是k，因为while会删除比本身小的元素
        if idx >= k and window[0] <= idx - k:
            window.pop(0)
        # 入队时，判断当前元素与上一个元素的大小，如果比上一个元素大，则将上一个元素出栈，这样保证了最左边的元素
        # 一直是最大的元素。
        while window and nums[window[-1]] <= num:
            window.pop()

        window.append(idx)

        if idx >= k - 1:
            res.append(nums[window[0]])

    return res


res = max_sliding_window([1, -3, 5, -1, 2], 3)
print(res)
