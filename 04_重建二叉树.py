# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/23 9:52
# @Ide     : PyCharm
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0 or len(pre) != len(tin):
            return None
        parent_val = pre[0]
        parent_i = 0
        for i, val in enumerate(tin):
            if val == parent_val:
                parent_i = i

        parent_node = TreeNode(parent_val)
        parent_node.left = self.reConstructBinaryTree(pre[1:parent_i + 1], tin[:parent_i])
        parent_node.right = self.reConstructBinaryTree(pre[parent_i + 1:], tin[parent_i + 1:])
        return parent_node
