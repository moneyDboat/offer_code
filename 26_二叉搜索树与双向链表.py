# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/28 3:01
# @Ide     : PyCharm
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return None
        pre = None
        self.ConvertCore(pRootOfTree, pre)

        listHead = pRootOfTree
        while listHead.left:
            listHead = listHead.left
        return listHead

    def ConvertCore(self, root, pre):
        if root is None:
            return pre
        pre = self.ConvertCore(root.left, pre)
        root.left = pre
        if pre:
            pre.right = root
        pre = root
        pre = self.ConvertCore(root.right, pre)

        return pre
