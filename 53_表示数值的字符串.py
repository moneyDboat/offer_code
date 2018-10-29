# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:21
# @Ide     : PyCharm
"""
import re


class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        # 字符串匹配类型的题目使用正则表达式是最方便的
        return re.match(r"^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$", s)
