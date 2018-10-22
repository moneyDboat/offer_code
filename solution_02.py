# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/22 23:41
# @Ide     : PyCharm
"""


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        if s is None:
            return None
        # return s.replace(' ', '%20')
        new_s = ''
        for s_i in s:
            if s_i == ' ':
                new_s += '%20'
            else:
                new_s += s_i
        return new_s
