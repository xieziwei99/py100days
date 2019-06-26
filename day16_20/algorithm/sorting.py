#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 排序
@author: xieziwei99
@Create Date: 2019/6/22
"""


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        # 3.6新特性，f-string
        return f'{self.name}: {self.age}'

    def __repr__(self):
        return self.__str__()

    def __le__(self, other):
        return self.age <= other.age


def select_sort(origin_items: list, *, comp=lambda x, y: x < y):
    """
    简单选择排序
    :param origin_items: 带排序的list或tuple
    :param comp: 比较条件【可选】，默认为：lambda x, y: x < y，即x<y时返回True
    :return: 排序好的list或tuple，默认升序
    """
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        # 找到索引i及其之后所有元素中最小元素的索引
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        # 互换第i号元素和其后最小元素的位置
        # 在python中，不需要temp就能互换
        items[i], items[min_index] = items[min_index], items[i]
    return items


def bubble_sort(origin_items: list, *, comp=lambda x, y: x < y):
    """ 冒泡排序 """
    items = origin_items[:]
    for i in range(0, len(items) - 1):  # i代表比较趟数，为n-1
        swapped = False
        # 一趟下来最大值则移到最右边
        for j in range(0, len(items) - i - 1):
            if comp(items[j + 1], items[j]):  # 若右边<左边，则交换
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items


def quick_sort(origin_items: list, *, comp=lambda x, y: x <= y):
    """
    快速排序
    :param origin_items: 待排序序列
    :param comp: 比较函数，若结果要升序，则传入 x <= y
    :return: 排好序的序列
    """
    items = origin_items[:]
    _quick_sort(items, 0, len(items)-1, comp)
    return items


def _quick_sort(items, low, high, comp):
    if low < high:
        pivot_pos = _partition(items, low, high, comp)
        _quick_sort(items, low, pivot_pos-1, comp)
        _quick_sort(items, pivot_pos+1, high, comp)


def _partition(items, low, high, comp):
    """
    快速排序一次划分
    :param items: 待排序序列
    :param low: 划分的起点
    :param high: 划分的终点
    :param comp: 比较函数，若结果要升序，则传入 x <= y
    :return: 一次划分后分界点的位置
    """
    temp = items[low]
    pivot = items[low]
    while low < high:
        # 从右往左找到第一个比pivot小的，移到low的位置
        while low < high and comp(pivot, items[high]):
            high -= 1
        items[low] = items[high]
        # 从左往右找到第一个比pivot大的，移到high位置
        while low < high and comp(items[low], pivot):
            low += 1
        items[high] = items[low]
    items[low] = temp
    return low  # 返回划分后的分界点


def merge_sort(origin_items: list, *, comp=lambda x, y: x <= y):
    """
    归并排序
    :param origin_items: 带排序序列
    :param comp: 比较函数，若结果要升序，则传入 x <= y
    :return: 排好序的序列
    """
    items = origin_items[:]
    if len(items) < 2:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right, comp)


def merge(items1, items2, comp=lambda x, y: x <= y):
    """
    合并两个序列
    :param items1: 序列1
    :param items2: 序列2
    :param comp: 比较函数，若结果要升序，则传入 x <= y
    :return: 合并后的序列
    """
    items = []
    i1, i2 = 0, 0
    while i1 < len(items1) and i2 < len(items2):
        if comp(items1[i1], items2[i2]):
            items.append(items1[i1])
            i1 += 1
        else:
            items.append(items2[i2])
            i2 += 1
    items += items1[i1:]
    items += items2[i2:]
    return items


def main():
    t = [1, 4, 7, 2, 9, 8, 3, 5, 6]
    print(t)
    print(select_sort(t))
    print(bubble_sort(t))
    print(quick_sort(t))
    print(merge_sort(t))

    t2 = [
        Person('Wang', 25), Person('Luo', 39),
        Person('Zack', 50), Person('He', 20)
    ]
    print(select_sort(t2, comp=lambda p1, p2: p1.age < p2.age))
    print(bubble_sort(t2, comp=lambda p1, p2: p1.name < p2.name))
    print(quick_sort(t2))   # 重写了__le__方法
    print(merge_sort(t2))


if __name__ == '__main__':
    main()
