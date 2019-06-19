"""
Created on 2019/6/19

@author: xieziwei99
"""
from socket import socket, AF_INET, SOCK_DGRAM


def main():
	client = socket(AF_INET, SOCK_DGRAM)
	while True:
		data_str = input('Please input: ')
		client.sendto(data_str.encode('utf-8'), ('localhost', 6666))
		data, addr = client.recvfrom(1024)
		data_str = data.decode('utf-8')
		print('Server response: ', data_str)
		if 'byetoo' == data_str:
			break
	client.close()


if __name__ == '__main__':
	main()