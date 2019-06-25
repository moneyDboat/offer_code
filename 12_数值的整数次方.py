# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/24 13:03
# @Ide     : PyCharm
"""


class Solution:
    def Power(self, base, exponent):
        # 常规解法
        # if exponent == 1:
        #     return base
        # elif exponent == -1:
        #     return base ** -1
        # elif exponent == 0:
        #     return 1
        # if exponent % 2 == 1:
        #     return self.Power(base, exponent >> 1) ** 2 * base
        # else:
        #     return self.Power(base, exponent >> 1) ** 2

        # python特色解法
        return base ** exponent
