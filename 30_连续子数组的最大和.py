# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/28 16:04
# @Ide     : PyCharm
"""


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        # 动态规划
        max_res = list()
        max_res.append(array[0])
        for i in range(1, len(array)):
            max_res.append(max(array[i], max_res[i - 1] + array[i]))

        return max(max_res)
