# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/28 16:08
# @Ide     : PyCharm
"""


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        # 重点是定义一个比较函数
        if not numbers:
            return ""
        return "".join(map(str, sorted(numbers, self.compare)))

    def compare(self, a, b):
        if int(str(a) + str(b)) <= int(str(b) + str(a)):
            return -1
        else:
            return 1
