# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/23 0:00
# @Ide     : PyCharm
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode is None:
            return []
        # 因为append()没有返回值，所以这里不能用
        return self.printListFromTailToHead(listNode.next) + [listNode.val]
