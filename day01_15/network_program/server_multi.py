"""
Created on 2019/6/19
Server using multi-threading
@author: xieziwei99
"""
from base64 import b64encode
from json import dumps
from socket import socket
from threading import Thread


def main():

	class FileTransferHandler(Thread):

		def __init__(self, cli, data1):
			super().__init__()
			self.cli = cli  # type: socket
			self.data = data1

		def run(self):
			my_dict = {'filename': 'guido.jpg', 'file_data': self.data}
			json_str = dumps(my_dict)
			self.cli.send(json_str.encode('utf-8'))
			self.cli.close()

	server = socket()
	server.bind(('localhost', 6666))
	server.listen(1024)
	print('Server started...')
	with open('guido.jpg', 'rb') as f:
		# 将二进制数据处理成base64再解码成字符串
		# Base64是一种用64个字符表示所有二进制数据的编码方式，通过将二进制数据每6位一组的方式重新组织，
		# 刚好可以使用0~9的数字、大小写字母以及“+”和“/”总共64个字符表示从000000到111111的64种状态
		data = b64encode(f.read()).decode('utf-8')
	while True:
		client, addr = server.accept()
		FileTransferHandler(client, data).start()


if __name__ == '__main__':
	main()