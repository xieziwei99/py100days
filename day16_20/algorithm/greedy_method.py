#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 贪婪算法，在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解
假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品。
很显然，他不能把所有物品都装进背包，所以必须确定拿走哪些物品，留下哪些物品
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
@author: xieziwei99
@Create Date: 2019/6/28
"""


class Thing(object):

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        """ 价格重量比 """
        return self.price / self.weight


def input_thing():
    name, price, weight = input("请输入物品信息：").split()
    return name, int(price), int(weight)


def main():
    # split() 默认以空白字符作为分隔符，并在结果中丢弃空白符
    # map() 将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
    max_weight, num_of_things = map(int, input("请输入总重量和物品总件数：").split())
    all_things = []
    for _ in range(num_of_things):
        # Python允许在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
        all_things.append(Thing(*input_thing()))
    # 以thing.value作为key来排序，并降序排列
    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight, total_price = 0, 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'小偷共偷走{total_price}元钱')


if __name__ == '__main__':
    main()