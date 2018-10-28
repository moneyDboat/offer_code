# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/27 11:34
# @Ide     : PyCharm
"""


class Solution:
    stack = []
    min_stack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.min_stack:
            tmp_min = self.min_stack[-1]
            self.min_stack.append(min(node, tmp_min))
        else:
            self.min_stack.append(node)

    def pop(self):
        # write code here
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.min_stack[-1]