# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/28 3:02
# @Ide     : PyCharm
"""


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        tmpNumber = None
        times = 0
        for number in numbers:
            if times == 0:
                tmpNumber = number
                times = 1
            elif tmpNumber == number:
                times += 1
            elif tmpNumber != number:
                times -= 1

        times = 0
        for number in numbers:
            if number == tmpNumber:
                times += 1
        if times > len(numbers) / 2:
            return tmpNumber
        else:
            return 0
