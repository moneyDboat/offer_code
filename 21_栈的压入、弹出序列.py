# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/27 11:35
# @Ide     : PyCharm
"""


class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        i, j = 0, 0
        while j < len(popV):
            if stack and popV[j] == stack[-1]:
                stack.pop()
                j += 1
            else:
                while True:
                    if i == len(pushV):
                        return False
                    if pushV[i] == popV[j]:
                        i += 1
                        j += 1
                        break
                    stack.append(pushV[i])
                    i += 1

        return True
