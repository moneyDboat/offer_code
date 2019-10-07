# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/28 16:04
# @Ide     : PyCharm
"""


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        # 快速排序
        def quick_sort(lst):
            if not lst:
                return []
            pivot = lst[0]
            left = quick_sort([x for x in lst[1:] if x < pivot])
            right = quick_sort([x for x in lst[1:] if x >= pivot])
            return left + [pivot] + right

        if not tinput or k > len(tinput):
            return []
        tinput = quick_sort(tinput)
        return tinput[:k]
