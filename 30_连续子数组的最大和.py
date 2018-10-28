# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/28 16:04
# @Ide     : PyCharm
"""


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return None
        maxSum = array[0]
        tmpSum = array[0]
        for i in range(1, len(array)):
            if tmpSum > 0:
                tmpSum += array[i]
            else:
                tmpSum = array[i]
            maxSum = max(maxSum, tmpSum)

        return maxSum