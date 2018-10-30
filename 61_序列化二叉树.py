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
    def Serialize(self, root):
        # 使用前序遍历
        ret = []
        if not root:
            return '#'
        ret.append(str(root.val))
        l = self.Serialize(root.left)
        ret.append(l)
        r = self.Serialize(root.right)
        ret.append(r)
        return ','.join(ret)

    def Deserialize(self, s):
        serialize = s.split(',')
        tree, sp = self.desCore(serialize, 0)
        return tree

    def desCore(self, s, sp):
        if sp >= len(s) or s[sp] == "#":
            return None, sp + 1
        node = TreeNode(int(s[sp]))
        sp += 1
        node.left, sp = self.desCore(s, sp)
        node.right, sp = self.desCore(s, sp)
        return node, sp