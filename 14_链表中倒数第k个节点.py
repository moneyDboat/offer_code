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
        # 双指针解法
        front, back = head, head
        while k:
            if not front:
                return None
            front = front.next
            k -= 1
        while front:
            front, back = front.next, back.next
        return back
