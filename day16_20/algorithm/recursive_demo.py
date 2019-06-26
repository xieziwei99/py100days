#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 函数递归调用
@author: xieziwei99
@Create Date: 2019/6/24
"""
from contextlib import contextmanager
from time import perf_counter


def fib(num):
    """ 最直接的递归实现 """
    assert num > 0
    if num in (1, 2):
        return 1
    return fib(num-1) + fib(num-2)


def fib1(num):
    """ 生成器实现Fibonacci """
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a+b
        yield a


# 动态规划 - 自顶向下的备忘录法：将求出的解用数组保存起来，下次再用时，直接取
def fib2(num, results=None):
    if results is None:
        results = {}
    assert num > 0
    if num in (1, 2):
        return 1
    try:
        return results[num]
    except KeyError:
        results[num] = fib2(num-1, results) + fib2(num-2, results)
        return results[num]


# 动态规划 - 自底向上的动态规划：先计算子问题，再由子问题计算父问题
def fib3(num):
    assert num > 0
    results = {1: 1, 2: 1}
    for i in range(3, num+1):
        results[i] = results[i-1] + results[i-2]
    return results[num]


# 上面的函数fib3使用了results[1] ~ results[num]个空间
# 但实际参与循环的只有2个值，因此空间上可进一步压缩
def fib4(num):
    """ fib(1)=1 fib(2)=1 ... fib(n)=fib(n-1) + fib(n-2) """
    a, b = 1, 1
    for _ in range(num - 1):
        a, b = b, a+b
    return a


@contextmanager     # 通过这个，可以实现with结果
def timer():
    try:
        # time(), perf_counter(), process_time()，都可用于程序性能计时
        # time()精度上相对没有那么高，而且受系统的影响，适合表示日期时间或者大程序程序的计时。
        # 通常perf_counter()用在测试代码时间上，具有最高的可用分辨率
        # perf_counter()会包含sleep()休眠时间，适用测量短持续时间
        # process_time()功能与此类似，但不包括sleep()休眠时间期间经过的时间
        start = perf_counter()
        yield
    finally:
        end = perf_counter()
        print(f'{end - start}秒')


def main():
    print(fib(20))
    print(fib4(3))
    print(fib2(5))
    print(fib3(6))
    for f in fib1(10):
        print(f, end=" ")
    print()

    with timer():
        print(f'20: {fib(20)}')
    with timer():
        print(f'100: {fib2(100)}')
    with timer():
        print(f'100: {fib3(100)}')
    with timer():
        print(f'100: {fib4(100)}')


if __name__ == '__main__':
    main()