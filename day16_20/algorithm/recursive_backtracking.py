#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description:
    递归回溯法：叫称为试探法，按选优条件向前搜索，当搜索到某一步，
        发现原先选择并不优或达不到目标时，就退回一步重新选择。
    经典问题：骑士巡逻，找出所有的骑士巡逻路径。
        按照骑士的走法走遍整个棋盘的每一个方格，而且每个网格只能夠经过一次。
        假若騎士能夠從走回到最初位置，则称此巡逻为封闭巡逻。
@author: xieziwei99
@Create Date: 2019/6/29
"""

SIZE = 5
total = 0


def print_board(board):
    for row in board:
        for col in row:
            # In [2]: '3'.center(5)
            # Out[2]: '  3  '
            print(str(col).center(4), end=' ')
        print()


def patrol(board, row, col, step=1):
    if 0 <= row < SIZE and 0 <= col < SIZE and 0 == board[row][col]:    # board初始化为0，代表未走过
        board[row][col] = step
        if step == SIZE * SIZE:
            global total
            total += 1
            print(f'第{total}种走法：')
            print_board(board)
        patrol(board, row - 2, col - 1, step + 1)
        patrol(board, row - 1, col - 2, step + 1)
        patrol(board, row + 1, col - 2, step + 1)
        patrol(board, row + 2, col - 1, step + 1)
        patrol(board, row + 2, col + 1, step + 1)
        patrol(board, row + 1, col + 2, step + 1)
        patrol(board, row - 1, col + 2, step + 1)
        patrol(board, row - 2, col + 1, step + 1)
        board[row][col] = 0     # TODO: 不明白


def main():
    # In [3]: [0] * 5
    # Out[3]: [0, 0, 0, 0, 0]
    board = [[0] * SIZE for _ in range(SIZE)]
    patrol(board, SIZE-1, SIZE-1)


if __name__ == '__main__':
    main()