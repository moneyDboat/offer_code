# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/28 3:01
# @Ide     : PyCharm
"""


class Solution:
    def Permutation(self, ss):
        # write code here
        # 递归，python中str类型无法修改，所以需要先转换成列表再进行处理
        if not ss:
            return []
        res = []
        self.Core(res, list(ss), 0)
        return sorted(res)

    def Core(self, res, ss, i):
        if i == len(ss) - 1:
            res.append("".join(ss))
        else:
            for j in range(i, len(ss)):
                # 可能有字符重复
                if i != j and ss[i] == ss[j]:
                    continue
                ss[i], ss[j] = ss[j], ss[i]
                # 按值传递
                self.Core(res, ss, i + 1)
                ss[j], ss[i] = ss[i], ss[j]
