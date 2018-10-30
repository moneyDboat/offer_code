# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:26
# @Ide     : PyCharm
"""


class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or size > len(num) or size <= 0:
            return []
        res = [max(num[0:size])]
        last = num[0]
        for i in range(1, len(num) - size + 1):
            if res[i - 1] == last:
                res.append(max(num[i:i + size]))
            else:
                res.append(max(res[i - 1], num[i + size - 1]))
            last = num[i]

        return res
