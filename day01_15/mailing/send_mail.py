"""
Created on 2019/6/19
Send simple mail
Send mail with attachment
@author: xieziwei99
"""
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP


def main():
	sender = '1374884318@qq.com'
	receivers = ['xieziwei@bupt.edu.cn', 'xieziwei99@gmail.com']
	message = MIMEText('A mail sent using python', 'plain', 'utf-8')
	message['From'] = Header('Jack', 'utf-8')
	message['To'] = Header('Kinking', 'utf-8')
	message['Subject'] = Header('A mail demo', 'utf-8')
	smtper = SMTP('smtp.qq.com')    # the host of sender
	# 登录到SMTP服务器
	# 请注意此处不是使用密码而是邮件客户端授权码进行登录
	smtper.login(sender, 'syfvjgnidvkggjhd')
	smtper.sendmail(sender, receivers, message.as_string())
	smtper.quit()
	print('Mail sent')


def main1():
	# 创建一个带附件的邮件消息对象
	message = MIMEMultipart()
	# 创建文本内容
	text_content = MIMEText('附件中有一张图片', 'plain', 'utf-8')
	message['Subject'] = Header('万里花图片', 'utf-8')
	# 将文本内容添加到邮件消息对象中
	message.attach(text_content)

	image_file = 'wlh.jpg'
	image_part = MIMEImage(open(image_file, 'rb').read(), image_file.split('.')[-1])
	image_part.add_header('Content-Disposition', 'attachment', filename=image_file)
	message.attach(image_part)

	# 创建SMTP对象
	smtper = SMTP('smtp.qq.com')
	sender = '1374884318@qq.com'
	receivers = ['xieziwei@bupt.edu.cn', 'xieziwei99@gmail.com']
	smtper.login(sender, 'syfvjgnidvkggjhd')
	smtper.sendmail(sender, receivers, message.as_string())
	smtper.quit()
	print('Mail with attachment sent')


if __name__ == '__main__':
	main()
	main1()
