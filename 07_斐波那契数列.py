# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/23 11:08
# @Ide     : PyCharm
"""


class Solution:
    def Fibonacci(self, n):
        # write code here
        # 直接递归会超时，需要使用动态规划的思想
        res = [0, 1]
        while len(res) <= n:
            res.append(res[-1] + res[-2])
        return res[n]
