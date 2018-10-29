# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:22
# @Ide     : PyCharm
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return None

        # 在原链表前新建一个头结点
        new_head = ListNode(0)
        new_head.next = pHead

        pre_p = new_head
        tmp_p = pHead

        while tmp_p:
            next_p = tmp_p.next
            if next_p and next_p.val == tmp_p.val:
                while next_p and next_p.val == tmp_p.val:
                    next_p = next_p.next
                pre_p.next = next_p
            else:
                pre_p = tmp_p
            tmp_p = next_p

        return new_head.next
