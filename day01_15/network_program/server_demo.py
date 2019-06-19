"""
Created on 2019/6/19
To send the time as a server
@author: xieziwei99
"""
import datetime
import socket


def main():
	server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
	server.bind(('localhost', 6666))    # the param-address is formed to a tuple
	server.listen(512)
	print('Server started...')
	while True:
		client, addr = server.accept()
		print(addr, 'connected to the server')
		client.send(str(datetime.datetime.now()).encode('utf8'))   # send to client
		client.close()


if __name__ == '__main__':
	main()