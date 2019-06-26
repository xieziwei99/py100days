"""
Created on 2019/6/19
使用pillow操作图像
@author: xieziwei99
"""
from PIL import Image


def main():
	img = Image.open('./network_program/upload/guido.jpg')
	print(img.size, img.format, img.format_description)
	img.save('./network_program/upload/guido.png')

	img2 = Image.open('./network_program/upload/guido.png')
	img3 = img2.crop((335, 435, 430, 615))
	for x in range(4):
		for y in range(5):
			img2.paste(img3, (95 * y, 180 * x))
	img2.resize((img.size[0] // 2, img.size[1] // 2))
	img2.rotate(90)
	img2.save('./network_program/upload/guido2.png')


if __name__ == '__main__':
	main()