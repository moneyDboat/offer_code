# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:20
# @Ide     : PyCharm
"""


class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return None

        head = [1]
        tail = [1]
        for i in range(len(A) - 1):
            head.append(A[i] * head[i])
            tail.append(A[-i - 1] * tail[i])
        return [head[j] * tail[-j - 1] for j in range(len(head))]
