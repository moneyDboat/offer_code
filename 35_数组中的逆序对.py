# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/28 16:09
# @Ide     : PyCharm
"""


class Solution:
    def InversePairs(self, data):
        # write code here
        return self.inverseCount(data[:], 0, len(data) - 1, data[:]) % 1000000007

    def inverseCount(self, tmp, start, end, data):
        if end - start < 1:
            return 0
        if end - start == 1:
            if data[start] <= data[end]:
                return 0
            else:
                tmp[start], tmp[end] = data[end], data[start]
                return 1
        mid = (start + end) // 2
        cnt = self.inverseCount(data, start, mid, tmp) + self.inverseCount(data, mid + 1, end, tmp)
        # print(start, mid, end, cnt, data)
        i = start
        j = mid + 1
        ind = start

        while i <= mid and j <= end:
            if data[i] <= data[j]:
                tmp[ind] = data[i]
                i += 1
            else:
                tmp[ind] = data[j]
                cnt += mid - i + 1
                j += 1
            ind += 1
        while i <= mid:
            tmp[ind] = data[i]
            i += 1
            ind += 1
        while j <= end:
            tmp[ind] = data[j]
            j += 1
            ind += 1
        return cnt