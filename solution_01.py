# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/22 23:06
# @Ide     : PyCharm
"""


class Solution:
    # array 二维列表
    def Find(self, target, array):
        if array is None or target is None:
            return None
        rows, cols = len(array), len(array[0])

        i, j = 0, cols - 1
        while (i < rows and j >= 0):
            tmp = array[i][j]
            if tmp == target:
                return True
            elif tmp > target:
                j -= 1
            elif tmp < target:
                i += 1
        return False
