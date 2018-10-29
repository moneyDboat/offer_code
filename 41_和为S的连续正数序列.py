# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:14
# @Ide     : PyCharm
"""


class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        tmp = [1, 2]
        a, b = 1, 2
        tmp_sum = a + b

        while b <= (tsum + 1) / 2:
            if tmp_sum <= tsum:
                if tmp_sum == tsum:
                    res.append(tmp[:])
                b += 1
                tmp.append(b)
                tmp_sum += b
            elif tmp_sum > tsum:
                tmp = tmp[1:]
                tmp_sum -= a
                a += 1

        return res
