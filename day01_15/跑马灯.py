'''
Created on 2019年06月10日
在屏幕上显示跑马灯文字
@author: xieziwei99
'''
import os, time

def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.1)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()