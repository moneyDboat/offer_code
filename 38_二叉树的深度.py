# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:12
# @Ide     : PyCharm
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        left_depth = self.TreeDepth(pRoot.left)
        right_depth = self.TreeDepth(pRoot.right)
        return max(left_depth, right_depth) + 1