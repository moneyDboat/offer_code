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
        if not pHead:
            return pHead
        pre = None
        while pHead.next:
            nex = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = nex
        pHead.next = pre
        return pHead
