# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:22
# @Ide     : PyCharm
"""


class Solution:
    def __init__(self):
        self.char_list = [-1 for i in range(256)]
        self.index = 0  # 记录当前字符的个数，可以理解为输入的字符串中的下标

    '''
    解法：利用一个int型数组表示256个字符，这个数组初值置为-1.
    每读出一个字符，将该字符的位置存入字符对应数组下标中。
    若值为-1标识第一次读入，不为-1且>0表示不是第一次读入，将值改为-2.
    之后在数组中找到>0的最小值，该数组下标对应的字符为所求。
    在python中，ord(char)是得到char对应的ASCII码；chr(idx)是得到ASCII位idx的字符
    '''

    def FirstAppearingOnce(self):
        # write code here
        min_value = 500
        min_idx = -1
        for i in range(256):
            if self.char_list[i] > -1:
                if self.char_list[i] < min_value:
                    min_value = self.char_list[i]
                    min_idx = i
        if min_idx > -1:
            return chr(min_idx)
        else:
            return '#'

    def Insert(self, char):
        # 如果是第一出现，则将对应元素的值改为下边
        if self.char_list[ord(char)] == -1:
            self.char_list[ord(char)] = self.index
        # 如果已经出现过两次了，则不修改
        elif self.char_list[ord(char)] == -2:
            pass
        # 如果出现过一次，则进行修改，修改为-2
        else:
            self.char_list[ord(char)] = -2
        self.index += 1
