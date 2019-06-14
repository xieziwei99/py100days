'''
Created on 2019年06月10日
生成制定长度验证码
@author: xieziwei99
'''
import random

def generate_code(length=4):
    all_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(length):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code

def main():
    print(generate_code())

if __name__ == '__main__':
    main()