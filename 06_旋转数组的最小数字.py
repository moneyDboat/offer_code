# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/23 10:58
# @Ide     : PyCharm
"""


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # 不能直接遍历，需要使用二分法
        if len(rotateArray) == 0:
            return 0
        left, right = 0, len(rotateArray) - 1
        while left < right:
            mid = (left + right) / 2
            if rotateArray[mid] < rotateArray[right]:
                right = mid
            else:
                left = mid + 1
        return rotateArray[left]
