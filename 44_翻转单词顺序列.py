# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:16
# @Ide     : PyCharm
"""


class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s.strip():
            return s
        return " ".join(s.split()[::-1])