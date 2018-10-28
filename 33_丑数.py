# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/28 16:08
# @Ide     : PyCharm
"""


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        uglyNums = [1]
        a, b, c = 0, 0, 0
        for i in range(1, index):
            tmp = min(uglyNums[a] * 2, uglyNums[b] * 3, uglyNums[c] * 5)
            uglyNums.append(tmp)
            while uglyNums[a] * 2 <= tmp:
                a += 1
            while uglyNums[b] * 3 <= tmp:
                b += 1
            while uglyNums[c] * 5 <= tmp:
                c += 1

        return uglyNums[index - 1]