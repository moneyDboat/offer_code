# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/24 14:11
# @Ide     : PyCharm
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None:
            return pHead
        tmp_node = pHead.next
        pHead.next = None
        before_node = pHead
        while (tmp_node):
            next_node = tmp_node.next
            tmp_node.next = before_node
            before_node = tmp_node
            tmp_node = next_node

        return before_node
