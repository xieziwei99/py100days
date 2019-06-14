'''
Created on 2019年06月10日
生成器函数
@author: xieziwei99
'''
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        yield a

def main():
    for v in fib(20):
        print(v)

if __name__ == '__main__':
    main()