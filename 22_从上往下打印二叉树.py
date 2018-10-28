# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/27 11:36
# @Ide     : PyCharm
"""


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return []
        result = []
        stack = [root]
        while stack:
            new_stack = []
            for node in stack:
                result.append(node.val)
                if node.left is not None:
                    new_stack.append(node.left)
                if node.right is not None:
                    new_stack.append(node.right)
            stack = new_stack

        return result
