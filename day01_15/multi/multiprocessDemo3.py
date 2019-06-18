"""
Created on 2019/6/18
实现进程间的通信，只有队列q是同一个队列
@author: xieziwei99
"""
import multiprocessing
import os


def sub_task(q, cnt):
	print('子进程号：', os.getpid())
	# cnt = 0
	while cnt < 10:
		q.put('pong')
		cnt += 1


def main():
	print('当前进程号：', os.getpid())
	q = multiprocessing.Queue()
	cnt = 0
	p = multiprocessing.Process(target=sub_task, args=(q, cnt))
	p.start()
	while cnt < 10:
		q.put('ping')
		cnt += 1
	p.join()
	for i in range(20):
		print(q.get(), end=' ')


if __name__ == '__main__':
	main()