# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/22 23:06
# @Ide     : PyCharm
"""


# 思路
# 矩阵是有序的，从左下角来看，向上数字递减，向右数字递增，
# 因此从左下角开始查找，当要查找数字比左下角数字大时。右移
# 要查找数字比左下角数字小时，上移


class Solution:
    # array 二维列表
    def Find(self, target, array):
        if array is None or target is None:
            return None
        rows, cols = len(array), len(array[0])

        i, j = 0, cols - 1
        while i < rows and j >= 0:
            tmp = array[i][j]
            if tmp == target:
                return True
            elif tmp > target:
                j -= 1
            elif tmp < target:
                i += 1
        return False
