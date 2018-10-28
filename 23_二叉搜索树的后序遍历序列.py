# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/28 0:44
# @Ide     : PyCharm
"""


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence is None or not sequence:
            return False
        return self.VerifyCore(sequence)

    def VerifyCore(self, sequence):
        if not sequence:
            return True
        root = sequence[-1]
        tmp = 0
        while sequence[tmp] < root:
            tmp += 1
        for val in sequence[tmp:-1]:
            if val < root:
                return False
        return self.VerifyCore(sequence[:tmp]) and self.VerifyCore(sequence[tmp:-1])
