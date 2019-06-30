#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 迭代工具 - 排列 / 组合 / 笛卡尔积
@author: xieziwei99
@Create Date: 2019/6/29
"""
import itertools


def main():
    for i in itertools.permutations('abc'):     # 排列
        print(i, end=' ')
    print()
    for i in itertools.combinations('abcd', 3):    # 组合
        print(i, end=' ')
    print()
    for i in itertools.product('abc', '12'):    # 笛卡尔积
        print(i, end=' ')
    print()


if __name__ == '__main__':
    main()
