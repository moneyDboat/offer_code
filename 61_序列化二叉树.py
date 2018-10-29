# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:25
# @Ide     : PyCharm
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 使用前序遍历
    def Serialize(self, root):
        # write code here
        if not root:
            return 'None'
        res = str(root.val)
        return res + ' ' + self.Serialize(root.left) + ' ' + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        if s == 'None':
            return None
        node_list = s.split()
        length = len(node_list)
        root = TreeNode(int(node_list[0]))
        root.left = self.Deserialize(' '.join(node_list[1:(length + 1) / 2]))
        root.right = self.Deserialize(' '.join(node_list[(length + 1) / 2:]))
        return root
