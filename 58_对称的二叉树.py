# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:23
# @Ide     : PyCharm
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        return self.core(pRoot.left, pRoot.right)

    def core(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return self.core(left.left, right.right) and self.core(left.right, right.left) and left.val == right.val
