# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/24 14:10
# @Ide     : PyCharm
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        first, second = head, head
        while k:
            if first is None:
                return None
            first = first.next
            k -= 1
        while first:
            first = first.next
            second = second.next
        return second
