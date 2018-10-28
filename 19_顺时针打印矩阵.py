# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/27 11:34
# @Ide     : PyCharm
"""


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        h, w = len(matrix), len(matrix[0])
        tmp = 0
        while tmp < float(h - 1) / 2 and tmp < float(w - 1) / 2:
            res += [matrix[tmp][i] for i in range(tmp, w - tmp)]
            res += [matrix[i][w - tmp - 1] for i in range(tmp + 1, h - tmp - 1)]
            res += [matrix[h - tmp - 1][i] for i in range(w - tmp - 1, tmp - 1, -1)]
            res += [matrix[i][tmp] for i in range(h - tmp - 2, tmp, -1)]
            tmp += 1
        if tmp == (h - 1) / 2:
            res += [matrix[tmp][i] for i in range(tmp, w - tmp)]
        elif tmp == (w - 1) / 2:
            res += [matrix[i][tmp] for i in range(tmp, h - tmp)]

        return res
