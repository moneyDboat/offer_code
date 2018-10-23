# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/23 12:18
# @Ide     : PyCharm
"""


class Solution:
    def rectCover(self, number):
        # write code here
        # 依然是斐波那契数列
        res = [0, 1, 2]
        while len(res) <= number:
            res.append(res[-1] + res[-2])
        return res[number]
