"""
Created on 2019/6/19
Client for multi-threading
@author: xieziwei99
"""
from base64 import b64decode
from json import loads
from socket import socket


def main():
	client = socket()
	client.connect(('localhost', 6666))
	in_data = bytes()
	# 由于不知道服务器发送的数据有多大每次接收1024字节
	data = client.recv(1024)
	while data:
		in_data += data
		data = client.recv(1024)
	my_dict = loads(in_data.decode('utf-8'))
	filename = my_dict['filename']
	file_data = my_dict['file_data'].encode('utf-8')
	with open('upload/' + filename, 'wb') as f:
		f.write(b64decode(file_data))
	print('Picture has been saved in current directory.')


if __name__ == '__main__':
	main()