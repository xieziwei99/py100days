#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 自定义字典，限制只有在key不存在时才能在dict中设置键值对。
@author: xieziwei99
@Create Date: 2019/7/17
"""


class SetOnceMappingMixin:

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(f'the key "{key}" already set')
        return super().__setitem__(key, value)


# 此类调用SetOnceMappingMixin的__setitem__
class SetOnceDict(SetOnceMappingMixin, dict):
    pass


# 涉及到菱形继承和C3算法
# 此类调用dict的__setitem__
class SetOnceDictFalse(dict, SetOnceMappingMixin):
    pass


def main():
    print(SetOnceDict.__mro__)
    print(SetOnceDictFalse.mro())
    my_dict = SetOnceDict()
    try:
        my_dict['name'] = 'Jack'
        my_dict['name'] = 'Rose'
    except KeyError as e:
        print(e)
    print(my_dict)

    my_dict_false = SetOnceDictFalse()
    try:
        my_dict_false['name'] = 'Jack'
        my_dict_false['name'] = 'Rose'
    except KeyError as e:
        print(e)
    print(my_dict_false)


if __name__ == '__main__':
    main()