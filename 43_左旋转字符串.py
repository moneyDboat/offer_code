# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:15
# @Ide     : PyCharm
"""


class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return ""
        s_len = len(s)
        n = n % s_len

        return s[n:] + s[:n]