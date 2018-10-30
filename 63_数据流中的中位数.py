# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:25
# @Ide     : PyCharm
"""


class Solution:
    def __init__(self):
        self.arr = []

    def Insert(self, num):
        self.arr.append(num)
        self.arr.sort()

    def GetMedian(self, fuck):
        length = len(self.arr)
        if length % 2 == 1:
            return self.arr[length // 2]
        return ((self.arr[length // 2] + self.arr[length // 2 - 1]) / 2.0)
