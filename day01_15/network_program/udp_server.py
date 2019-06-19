"""
Created on 2019/6/19

@author: xieziwei99
"""
from socket import socket, AF_INET, SOCK_DGRAM


def main():
	server = socket(family=AF_INET, type=SOCK_DGRAM)
	server.bind(('localhost', 6666))
	while True:
		data, addr = server.recvfrom(1024)  # 直接接收来自client发送的数据，而不需要等待client链接
		print('Received from', addr, ': ', data.decode('utf-8'))
		data = (data.decode('utf-8') + 'too').encode('utf-8')
		server.sendto(data, addr)
		if 'byetoo' == data.decode('utf-8'):
			break
	server.close()


if __name__ == '__main__':
	main()