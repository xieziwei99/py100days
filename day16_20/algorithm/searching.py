#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 顺序查找和二分查找
@author: xieziwei99
@Create Date: 2019/6/22
"""


# items: list，表示期望items的类型是list
# -> int，表示期望函数的返回值是int
# 这种写法，若不遵守也不会引起代码运行错误，最多由IDE给出警告
def seq_search(items: list, elem) -> int:
	"""
	顺序查找
	:param items: 类型为list，要查找的列表
	:param elem: 要查找的元素
	:return: 类型为int，找到返回索引，找不到返回-1
	"""
	for index, item in enumerate(items):
		if item == elem:
			return index
	return -1


def bi_search(items: list, elem) -> int:
	""" 二分查找 """
	start, end = 0, len(items) - 1
	while start <= end:
		mid = (start + end) // 2  # 与Java不同，这里要用//（地板除）
		if elem > items[mid]:
			start = mid + 1
		elif elem < items[mid]:
			end = mid - 1
		else:
			return mid
	return -1


def main():
	list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	print(seq_search(list1, 3))
	print(bi_search(list1, 10))


if __name__ == '__main__':
	main()