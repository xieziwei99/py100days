#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 求子列表元素之和的最大值
@author: xieziwei99
@Create Date: 2019/6/29
"""


# 时间复杂度为 O(n)
def solution1(t: list):
    if not [i for i in t if i > 0]:
        return max(t)
    temp = 0
    the_max = t[0]
    for i in range(len(t)):
        temp += t[i]
        if temp <= 0:
            temp = 0
        elif temp > the_max:
            the_max = temp
    return the_max


def main():
    t = list(map(int, input('请输入列表：').split()))
    print(solution1(t))


if __name__ == '__main__':
    main()