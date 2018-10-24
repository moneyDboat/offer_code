# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/24 14:09
# @Ide     : PyCharm
"""


class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = []
        even = []
        for a in array:
            if a % 2 == 1:
                odd.append(a)
            else:
                even.append(a)

        return odd + even
