# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/28 3:00
# @Ide     : PyCharm
"""


# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None

        tmpNode = pHead
        while tmpNode:
            copyNode = RandomListNode(tmpNode.label)
            copyNode.next = tmpNode.next
            forNode = tmpNode
            tmpNode = tmpNode.next
            forNode.next = copyNode

        tmpNode = pHead
        while tmpNode:
            if tmpNode.random:
                tmpNode.next.random = tmpNode.random.next
            tmpNode = tmpNode.next.next

        copyHead = pHead.next
        tmpNode = pHead
        while tmpNode:
            copyNode = tmpNode.next
            tmpNode.next = copyNode.next
            if tmpNode.next:
                copyNode.next = tmpNode.next.next
            else:
                copyNode.next = None
            tmpNode = tmpNode.next

        return copyHead
