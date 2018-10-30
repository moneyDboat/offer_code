# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:25
# @Ide     : PyCharm
"""


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        # 二叉搜索树的中序遍历即是正确的排序
        if not pRoot or k < 1:
            return None
        res = []
        self.KthCore(pRoot, res)
        if k <= len(res):
            return res[k - 1]
        else:
            return None

    def KthCore(self, pRoot, res):
        if not pRoot:
            return
        self.KthCore(pRoot.left, res)
        res.append(pRoot)
        self.KthCore(pRoot.right, res)
