# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:17
# @Ide     : PyCharm
"""


class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) != 5:
            return None
        numbers.sort()
        king_sum = sum([1 if number == 0 else 0 for number in numbers])
        needs = 0
        for i in range(king_sum + 1, 5):
            if numbers[i] == numbers[i - 1]:
                return False
            needs += numbers[i] - numbers[i - 1] - 1

        return needs <= king_sum
