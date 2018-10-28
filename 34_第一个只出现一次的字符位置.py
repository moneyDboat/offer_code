# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/28 16:08
# @Ide     : PyCharm
"""


class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        count = {}
        for letter in s:
            count[letter] = count.get(letter, 0) + 1

        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1
