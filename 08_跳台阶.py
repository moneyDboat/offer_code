# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/23 12:00
# @Ide     : PyCharm
"""


class Solution:
    def jumpFloor(self, number):
        # write code here
        res = [0, 1, 2]
        while len(res) <= number:
            res.append(res[-1] + res[-2])
        return res[number]
