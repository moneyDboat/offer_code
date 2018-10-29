# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:23
# @Ide     : PyCharm
"""


# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode.right:
            # 有右子树
            son_node = pNode.right
            while son_node.left:
                son_node = son_node.left
            return son_node
        else:
            # 无右子树，则找到第一个当前节点是父节点左子树的节点
            while pNode.next:
                if (pNode.next.left == pNode):
                    return pNode.next
                pNode = pNode.next  # 沿着父节点向上遍历
        return  # 到了根节点仍没找到，则返回空
