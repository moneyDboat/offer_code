# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:18
# @Ide     : PyCharm
"""


class Solution:
    def Add(self, num1, num2):
        # write code here
        # Python没有无符号右移操作
        # while num2:
        #     tmp = num1 ^ num2
        #     num2 = (num1 & num2) << 1
        #     num1 = tmp

        # return num1
        return sum([num1, num2])
