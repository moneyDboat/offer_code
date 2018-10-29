# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:20
# @Ide     : PyCharm
"""


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if not numbers:
            return False

        i = 0
        while i < len(numbers):
            if numbers[i] == i:
                i += 1
                continue
            if numbers[numbers[i]] == numbers[i]:
                duplication[0] = numbers[i]
                return True
            else:
                temp = numbers[i]
                numbers[i] = numbers[numbers[i]]
                numbers[temp] = temp

        return False