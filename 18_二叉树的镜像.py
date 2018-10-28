# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/27 11:33
# @Ide     : PyCharm
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None:
            return None
        tmp = root.left
        root.left = self.Mirror(root.right)
        root.right = self.Mirror(tmp)

        return root
