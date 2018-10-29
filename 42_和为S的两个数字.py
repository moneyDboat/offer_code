# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:15
# @Ide     : PyCharm
"""


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if array is None:
            return []
        start, end = 0, len(array) - 1
        while start < end:
            tmp = array[start] + array[end]
            if tmp < tsum:
                start += 1
            elif tmp > tsum:
                end -= 1
            elif tmp == tsum:
                # 最先找到的乘积就是最小的
                return [array[start], array[end]]

        return []