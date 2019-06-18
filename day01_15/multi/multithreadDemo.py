"""
Created on 2019/6/14
多线程示例
@author: xieziwei99
"""
import os
import random
import threading
import time


def download_task(filename):
	print('启动下载线程，进程号[%d]-线程号[%d].' % (os.getpid(), threading.get_ident()))
	print('开始下载%s...' % filename)
	t = random.randint(5, 10)
	time.sleep(t)
	print('%s下载完成! 耗费了%d秒' % (filename, t))


def main():
	start = time.time()
	p1 = threading.Thread(target=download_task, args=('Python从入门到住院.pdf', ))
	p1.start()
	p2 = threading.Thread(target=download_task, args=('Peking Hot.avi', ))
	p2.start()
	p1.join()
	p2.join()
	end = time.time()
	print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
	main()