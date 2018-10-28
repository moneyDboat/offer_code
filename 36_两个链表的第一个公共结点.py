# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/28 16:09
# @Ide     : PyCharm
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 is None or pHead2 is None:
            return None
        p1_len, p2_len = 0, 0
        p1, p2 = pHead1, pHead2
        while p1:
            p1_len += 1
            p1 = p1.next
        while p2:
            p2_len += 1
            p2 = p2.next

        if p1_len > p2_len:
            for i in range(p1_len - p2_len):
                pHead1 = pHead1.next
        else:
            for i in range(p2_len - p1_len):
                pHead2 = pHead2.next
        while pHead1:
            if pHead1.val == pHead2.val:
                return pHead1
            pHead1, pHead2 = pHead1.next, pHead2.next

        return None
