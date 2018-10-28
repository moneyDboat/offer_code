# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/27 11:31
# @Ide     : PyCharm
"""


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 is None or pRoot2 is None:
            return False
        result = self.SubtreeCore(pRoot1, pRoot2)
        if result:
            return True
        else:
            return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def SubtreeCore(self, pRoot1, pRoot2):
        if pRoot2 is None:
            return True
        if pRoot1 is None:
            return False
        if pRoot1.val == pRoot2.val:
            return self.SubtreeCore(pRoot1.left, pRoot2.left) and self.SubtreeCore(pRoot1.right, pRoot2.right)
        else:
            return False
