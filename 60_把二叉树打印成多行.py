# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:24
# @Ide     : PyCharm
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []

        res = []
        nodes = [pRoot]
        while nodes:
            tmp_nodes = []
            tmp_res = []
            for node in nodes:
                tmp_res.append(node.val)
                if node.left:
                    tmp_nodes.append(node.left)
                if node.right:
                    tmp_nodes.append(node.right)
            res.append(tmp_res)
            nodes = tmp_nodes

        return res
