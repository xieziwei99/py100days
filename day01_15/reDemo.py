"""
Created on 2019年6月14日
正则表达式使用示例
@author: xieziwei99
"""
import re


def main1():
	# 验证输入用户名和QQ号是否有效并给出对应的提示信息
	# 要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
	username = input('Input user name: ')
	while True:
		m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
		if not m1:
			username = input('Please input valid user name: ')
		else:
			break
	qq = input('Input qq: ')
	while True:
		m2 = re.match(r'^[1-9]\d{4,11}$', qq)
		if not m2:
			qq = input('Please input valid qq: ')
		else:
			break
	print('你输入的信息是有效的!')


def main2():
	""" 替换字符串中的不良内容 """
	sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
	purified = re.sub(r'[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔', '*', sentence, flags=re.IGNORECASE)
	print(purified)


def main3():
	""" 拆分长字符串 """
	poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
	sentence_list = re.split(r'[,.，。]', poem)   # 最后会多出一个空字符串
	print(sentence_list)


if __name__ == '__main__':
	# main1()
	# main2()
	main3()
