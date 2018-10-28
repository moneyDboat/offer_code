# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/28 16:04
# @Ide     : PyCharm
"""


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput):
            return []
        return sorted(tinput)[:k]
