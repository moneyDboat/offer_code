# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/22 23:41
# @Ide     : PyCharm
"""


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if s is None:
            return None
        # return s.replace(' ', '%20')
        new_s = ''
        for char in s:
            if char == ' ':
                new_s += '%20'
            else:
                new_s += char
        return new_s
