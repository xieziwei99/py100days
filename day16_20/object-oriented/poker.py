#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 扑克游戏
    经验：符号常量总是优于字面常量，枚举类型是定义符号常量的最佳选择
@author: xieziwei99
@Create Date: 2019/7/17
"""
import random
from enum import Enum, unique


# 默认情况下，不同的成员值允许相同。但是两个相同值的成员，第二个成员的名称被视作第一个成员的别名
# @unique 限制定义枚举时，不能定义相同值的成员
from random import randint


@unique
class Suite(Enum):
    """ 花色 """

    DIAMOND, CLUB, HEART, SPADE = range(4)

    def __lt__(self, other):
        return self.value < other.value


class Card(object):
    """ 包含花色和大小 """

    def __init__(self, suite: Suite, face):
        self.suite = suite
        self.face = face

    def show(self):
        suites = ['♦', '♣', '♥', '♠']
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '⑩', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]} {faces[self.face]}'

    def __str__(self):
        return self.show()

    def __repr__(self) -> str:
        return self.__str__()


class Poker(object):

    def __init__(self):
        self.index = 0  # 指定当前发那张牌
        self.cards = [Card(suite, face) for suite in Suite for face in range(1, 14)]

    def shuffle(self):
        """ 洗牌 """
        random.shuffle(self.cards)  # 随机打乱列表顺序
        self.index = 0

    def deal(self) -> Card:
        """ 发牌 每发一张牌，index += 1 故 index = 已发牌数 """
        card = self.cards[self.index]
        self.index += 1
        return card

    @property
    def has_more(self):
        return self.index < len(self.cards)


class Player(object):

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """ 摸一张牌 """
        self.cards.append(card)

    """
    比较规则为：输入一张card，返回一个tuple如 ('♦', 2)
    tuple比较大小规则：从第一个开始比较，一旦出现结果就停止，如：
    
    In [1]: (1, 1) < (1, 5)
    Out[1]: True
    
    In [2]: (2, 1) < (1, 5)
    Out[2]: False

    """
    def sort(self, comp=lambda card: (card.suite, card.face)):
        """ 整理手上的牌 """
        self.cards.sort(key=comp)


def my_shuffle(my_list: list):
    n = len(my_list)
    temp = None
    for i in range(n)[::-1]:    # 使列表反转
        temp = randint(0, i)    # a <= N <= b.
        my_list[i], my_list[temp] = my_list[temp], my_list[i]


def main():
    poker = Poker()
    poker.shuffle()
    my_shuffle(poker.cards)
    print(poker.cards)
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    while poker.has_more:
        for player in players:
            player.get_one(poker.deal())
    for player in players:
        player.sort()
        print(f'{player.name}: {player.cards}')


if __name__ == '__main__':
    main()
