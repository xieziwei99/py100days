#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 装饰器示例、装饰无参函数
    装饰器 - 装饰器中放置的通常都是横切关注（cross-concern）功能
    所谓横切关注功能就是很多地方都会用到但跟正常业务又逻辑没有必然联系的功能
    装饰器实际上是实现了设计模式中的代理模式 - AOP（面向切面编程）
@author: xieziwei99
@Create Date: 2019/6/30
"""


def check_pwd(func):
    def wrapper():
        print('Checking password...')
        func()

    return wrapper


# 因为check_pwd返回inner函数、所以deposit等同于inner函数
@check_pwd  # 相当于deposit = check_pwd(deposit)
def deposit():
    print('Depositing...')


@check_pwd
def withdraw():
    print('Withdrawing...')


def main():
    deposit()
    withdraw()


if __name__ == '__main__':
    main()
