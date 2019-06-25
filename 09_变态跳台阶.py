# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/23 12:12
# @Ide     : PyCharm
"""


class Solution:
    def jumpFloorII(self, number):
        # 常规思路
        # res = [0, 1]
        # while len(res) <= number:
        #     res.append(sum(res) + 1)
        # return res[number]

        # 更简洁的方法
        # return 2 ** (number - 1)

        # 使用移位运算符更快
        if number == 0:
            return 0
        return 1 << number - 1
