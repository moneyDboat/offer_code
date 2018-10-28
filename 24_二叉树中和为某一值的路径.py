# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/28 0:45
# @Ide     : PyCharm
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def FindPath(self, root, expectNumber):
        resList = []
        pathList = []

        def subFindPath(root):
            if root:
                pathList.append(root.val)
                if not root.right and not root.left and sum(pathList) == expectNumber:
                    resList.append(pathList[:])
                else:
                    subFindPath(root.left)
                    subFindPath(root.right)
                pathList.pop()

        subFindPath(root)
        return resList
