# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:26
# @Ide     : PyCharm
"""


class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        self.row, self.col = rows, cols
        self.dict = set()
        self.search(threshold, 0, 0)
        return len(self.dict)

    def judge(self, threshold, i, j):
        return sum(map(int, list(str(i)))) + sum(map(int, list(str(j)))) <= threshold

    def search(self, threshold, i, j):
        if not self.judge(threshold, i, j) or (i, j) in self.dict:
            return
        self.dict.add((i, j))
        if i != self.row - 1:
            self.search(threshold, i + 1, j)
        if j != self.col - 1:
            self.search(threshold, i, j + 1)
