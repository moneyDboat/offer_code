# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:19
# @Ide     : PyCharm
"""


class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0

        numlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-']
        sum = 0
        label = 1  # 正负数标记
        for string in s:
            if string in numlist:  # 如果是合法字符
                if string == '+':
                    label = 1
                    continue
                if string == '-':
                    label = -1
                    continue
                else:
                    sum = sum * 10 + numlist.index(string)
            if string not in numlist:
                # 非合法字符
                sum = 0
                break

        return sum * label
