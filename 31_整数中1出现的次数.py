# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/28 16:07
# @Ide     : PyCharm
"""


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        # 依次计算各个位数上出现1的个数
        result = 0
        divisor = 1
        while n / divisor >= 1:
            divisor *= 10
            tmp = n / divisor
            if n % divisor >= 2 * divisor / 10:
                tmp += 1
            elif n % divisor >= divisor / 10:
                result += n % (divisor / 10) + 1
            result += tmp * divisor / 10

        return result