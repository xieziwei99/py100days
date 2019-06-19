"""
Created on 2019/6/19
receive data from the server_demo
@author: xieziwei99
"""
from socket import socket


def main():
	client = socket()
	client.connect(('localhost', 6666))
	print(client.recv(1024).decode('utf8'))
	client.close()


if __name__ == '__main__':
	main()
