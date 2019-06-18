"""
Created on 2019/6/18
完成1~100000000求和的计算密集型任务
@author: xieziwei99
"""
from multiprocessing import Queue, Process
from time import time


def main():
	total = 0
	number_list = [x for x in range(1, 10000001)]
	start = time()
	for number in number_list:
		total += number
	print(total)
	end = time()
	print('Execute time: %.3fs' % (end - start))


def task_handler(current_list, result_queue):
	total = 0
	for num in current_list:
		total += num
	result_queue.put(total)


def main1():
	processes = []
	num_list = [x for x in range(1, 10000001)]
	result_queue = Queue()
	index = 0
	for _ in range(8):
		p = Process(target=task_handler, args=(num_list[index: index+1250000], result_queue))
		index += 1250000
		processes.append(p)
		p.start()
	start = time()
	for p in processes:
		p.join()
	total = 0
	while not result_queue.empty():
		total += result_queue.get()     # get()会删除取得的元素
	print(total)
	end = time()
	print('Execute time with 8 processes: %.3fs' % (end - start))


if __name__ == '__main__':
	main()
	main1()