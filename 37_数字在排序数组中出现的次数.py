# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:11
# @Ide     : PyCharm
"""


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        # 没使用二分法，只使用了最简单的遍历，时间复杂度O(n)
        if data is None:
            return None
        count = 0
        for number in data:
            if number == k:
                count += 1

        return count