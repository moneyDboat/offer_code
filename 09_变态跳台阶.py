# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/23 12:12
# @Ide     : PyCharm
"""


class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 0:
            return 0
        # 使用位移运算符更快
        return 1 << number - 1
