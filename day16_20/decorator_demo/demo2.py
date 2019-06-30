#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 装饰器示例、装饰有参函数、装饰有返回值函数（也可以装饰无参函数）
@author: xieziwei99
@Create Date: 2019/6/30
"""


def celebrator(func):
    def wrapper(*args, **kwargs):
        print('I am yours')
        ret = func(*args, **kwargs)  # 这里调用my_print()，输出a，并将a作为返回值赋给ret
        return ret

    return wrapper


# my_print = celebrator(my_print)
@celebrator
def my_print(a):  # 有返回值
    print(a)
    return a


@celebrator
def your_print(b):  # 无返回值
    print(b)


# 先执行my_print('Hello world')，打印I am yours，和Hello world，并返回ret，即Hello world
# 再执行your_print('Hi world')，打印 I am yours，和Hi world，没有返回值，所以ret = None，最后return None
# 最后执行print('Hello world', None)
def main():
    print(my_print('Hello world'), your_print('Hi world'), sep='---')


if __name__ == '__main__':
    main()

# 所以my_print(a)函数的功能为：
# 1. print('I am yours')
# 2. 执行 ret = func(*args, **kwargs)，即执行print(a)，再执行ret = a
# 3. 执行 return ret
# 所以my_print(a)的返回值为：a
