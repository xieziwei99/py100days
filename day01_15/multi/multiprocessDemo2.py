"""
Created on 2019/6/18
父进程在创建子进程时复制了进程及其数据结构
@author: xieziwei99
"""
from multiprocessing import Queue, Process
from time import sleep


def sub_task(name, q):
	while not q.empty():
		num = q.get()
		print('%d: %s' % (num, name))
		sleep(0.001)


def main():
	q = Queue(10)
	for num in range(1, 11):
		q.put(num)
	# 两个进程共享了队列q
	Process(target=sub_task, args=('ping', q)).start()
	Process(target=sub_task, args=('pong', q)).start()


if __name__ == '__main__':
	main()