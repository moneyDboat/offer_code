# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:13
# @Ide     : PyCharm
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        # 平衡二叉树：空树或者两个左右子树高度差不超过1
        # 并且左右子树也是平衡二叉树
        if pRoot is None:
            return True, 0
        if_balanced, height = self.BalCore(pRoot)
        return if_balanced

    def BalCore(self, pRoot):
        if pRoot is None:
            return True, 0
        left_bal, left_height = self.BalCore(pRoot.left)
        right_bal, right_height = self.BalCore(pRoot.right)
        if_balanced = left_bal and right_bal and abs(left_height - right_height) <= 1
        return if_balanced, max(left_height, right_height) + 1
