# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:17
# @Ide     : PyCharm
"""


class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        # 约瑟夫环问题
        # 最简单的解法就是模拟这个过程
        if n < 1:
            return -1

        con = list(range(n))
        final = -1
        start = 0
        while con:
            k = (start + m - 1) % n
            final = con.pop(k)
            n -= 1
            start = k

        return final
