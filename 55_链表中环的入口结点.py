# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:22
# @Ide     : PyCharm
"""


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None
        fast_p, slow_p = pHead, pHead
        loop = False
        while fast_p and fast_p.next:
            fast_p = fast_p.next.next
            slow_p = slow_p.next
            if fast_p.val == slow_p.val:
                loop = True
                break
        if not loop:
            return None

        tmp_p = fast_p
        fast_p = fast_p.next
        loop_len = 1
        while fast_p != tmp_p:
            fast_p = fast_p.next
            loop_len += 1
        first_p, last_p = pHead, pHead
        for i in range(loop_len):
            first_p = first_p.next
        while first_p.val != last_p.val:
            first_p = first_p.next
            last_p = last_p.next

        return first_p
