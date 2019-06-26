#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 作图：各时间复杂度的示意图
@author: xieziwei99
@Create Date: 2019/6/22
"""
from math import log2, factorial

import numpy
from matplotlib import pyplot


def main():
	num = 6
	styles = ['r-.', 'g-*', 'b-o', 'y-x', 'c-^', 'm-+', 'k-d']
	legends = ['y=log2(x)', 'y=x', 'y=x*log2(x)', 'y=x^2', 'y=x^3', 'y=3^x', 'y=x!']

	x_data = [x for x in range(1, num+1)]   # 横轴1~6
	y_data1 = [log2(y) for y in range(1, num+1)]
	y_data2 = [y for y in range(1, num+1)]
	y_data3 = [y * log2(y) for y in range(1, num+1)]
	y_data4 = [y ** 2 for y in range(1, num+1)]
	y_data5 = [y ** 3 for y in range(1, num+1)]
	y_data6 = [3 ** y for y in range(1, num+1)]
	y_data7 = [factorial(y) for y in range(1, num+1)]
	y_datas = [y_data1, y_data2, y_data3, y_data4, y_data5, y_data6, y_data7]
	for i, y_data in enumerate(y_datas):
		# matplotlib是一个绘图库
		# pyplot是matplotlib的一个基于状态的接口。它提供了一种类似于matlab的绘图方法
		pyplot.plot(x_data, y_data, styles[i])
	pyplot.legend(legends)
	pyplot.xticks(numpy.arange(1, 7, step=1))
	pyplot.yticks(numpy.arange(0, 751, step=50))
	pyplot.show()


if __name__ == '__main__':
	main()