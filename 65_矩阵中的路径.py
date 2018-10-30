# -*- coding: utf-8 -*-

"""
# @Author  : captain
# @Time    : 2018/10/30 1:26
# @Ide     : PyCharm
"""


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        self.col, self.row = cols, rows
        board = [list(matrix[cols * i:cols * i + cols]) for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == path[0]:
                    self.b = False
                    self.search(board, path[1:], [(i, j)], i, j)
                    if self.b:
                        return True
        return False

    def search(self, board, word, dict, i, j):
        if word == "":
            self.b = True
            return
        if j != 0 and (i, j - 1) not in dict and board[i][j - 1] == word[0]:
            self.search(board, word[1:], dict + [(i, j - 1)], i, j - 1)
        if i != 0 and (i - 1, j) not in dict and board[i - 1][j] == word[0]:
            self.search(board, word[1:], dict + [(i - 1, j)], i - 1, j)
        if j != self.col - 1 and (i, j + 1) not in dict and board[i][j + 1] == word[0]:
            self.search(board, word[1:], dict + [(i, j + 1)], i, j + 1)
        if i != self.row - 1 and (i + 1, j) not in dict and board[i + 1][j] == word[0]:
            self.search(board, word[1:], dict + [(i + 1, j)], i + 1, j)
