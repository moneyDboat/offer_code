# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/28 0:44
# @Ide     : PyCharm
"""


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        # 递归解决
        if not sequence:
            return False
        return self.VerifyCore(sequence)

    def VerifyCore(self, sequence):
        if len(sequence) <= 1:
            return True
        parent_val = sequence[-1]
        split_i = 0
        while sequence[split_i] < parent_val:
            split_i += 1
        left_part = sequence[:split_i]
        right_part = sequence[split_i:-1]
        if right_part and min(right_part) < parent_val:
            return False
        return self.VerifyCore(left_part) and self.VerifyCore(right_part)
