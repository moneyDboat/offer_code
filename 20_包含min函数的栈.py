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
        self.stack.append(node)
        min_val = node
        if self.min_stack:
            min_val = min(self.min_stack[-1], node)
        self.min_stack.append(min_val)

    def pop(self):
        if self.stack:
            self.min_stack.pop()
            return self.stack.pop()
        else:
            return None

    def top(self):
        if self.stack:
            return self.stack1[-1]
        else:
            return None

    def min(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None
