#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description:
    用Counter找出序列中出现次数最多的元素
@author: xieziwei99
@Create Date: 2019/6/29
"""
from collections import Counter


def main():
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
        'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
        'look', 'into', 'my', 'eyes', "you're", 'under'
    ]
    count = Counter(words)
    print(count.most_common(3))
    print(count.most_common(1)[0][1])


if __name__ == '__main__':
    main()