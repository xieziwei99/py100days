"""
Created on 2019/6/14
python 多进程示例
@author: xieziwei99
"""
import multiprocessing
import os
import random
import time


def download_task(filename):
    print('启动下载进程，进程号[%d].' % os.getpid())
    print('开始下载%s...' % filename)
    t = random.randint(5, 10)
    time.sleep(t)
    print('%s下载完成! 耗费了%d秒' % (filename, t))


def main():
    start = time.time()
    p1 = multiprocessing.Process(target=download_task, args=('Python从入门到住院.pdf', ))
    p1.start()
    p2 = multiprocessing.Process(target=download_task, args=('Peking Hot.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()