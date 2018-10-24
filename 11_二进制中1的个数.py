# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/24 12:45
# @Ide     : PyCharm
"""


class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        # 因为python的int是无线精度的，c++和java的int是32位的，
        # 所以python的负数相当于前面有无限个1，要对python的负数做处理
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            # 每做一次运算相当于把最右侧的1变成0，能做多少次这种运算就相当于有多少个1
            n &= n - 1
        return count
