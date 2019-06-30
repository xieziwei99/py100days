#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 装饰器示例 - 装饰器本身需要参数
@author: xieziwei99
@Create Date: 2019/6/30
参考自廖雪峰Python教程：https://www.liaoxuefeng.com/wiki/1016959663602400/1017451662295584
"""

from datetime import datetime

from functools import wraps


# 没有参数的装饰器log1
from inspect import isfunction


def log1(func):
    def wrapper(*args, **kwargs):
        print(f'call {func.__name__}')
        return func(*args, **kwargs)

    return wrapper


@log1
def now1():
    print(datetime.now())


# 带参数的装饰器
def log2(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'{text} {func.__name__}')
            return func(*args, **kwargs)

        return wrapper

    return decorator


# 3层嵌套效果为：now2 = log2('execute:')(now2)
# 1. 执行log2('execute:')，返回函数decorator
# 2. 执行decorator(now2)，返回函数wrapper
# 3. 执行 now2 = wrapper
@log2('execute:')
def now2():
    print(datetime.now())


# 上面两个函数now1()和now2()的__name__属性从原来的now1/2变成了wrapper
# 需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的

# 用functools.wraps的没有参数的装饰器
def log1plus(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'call {func.__name__}')
        return func(*args, **kwargs)
    return wrapper


@log1plus
def now1p():
    print(datetime.now())


# 用functools.wraps的带参数的装饰器
def log2plus(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'{text} {func.__name__}')
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log2plus('execute it:')
def now2p():
    print(datetime.now())


# 升级版 - 支持不带参数和带参数
def log(arg):
    if isfunction(arg):
        @wraps(arg)
        def wrapper(*args, **kwargs):
            print(f'call {arg.__name__}')
            return arg(*args, **kwargs)
        return wrapper
    elif isinstance(arg, str):
        def decorator(func):
            @wraps(func)
            def wrapper1(*args, **kwargs):
                print(f'{arg} {func.__name__}')
                return func(*args, **kwargs)
            return wrapper1
        return decorator


@log
def now3():
    print(datetime.now())


@log('the upgrade:')
def now4():
    print(datetime.now())


# 用类实现装饰器
class Log(object):

    def __init__(self, text='call'):
        self.text = text

    def __call__(self, func):   # 通过__call__魔术方法使得对象可以当成函数调用
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'{self.text} {func.__name__}')
            return func(*args, **kwargs)
        return wrapper


@Log('with class')
def now5():
    print(datetime.now())


def main():
    now1()
    now2()
    now1p()
    now2p()
    now3()
    now4()
    now5()


if __name__ == '__main__':
    main()
