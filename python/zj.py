# import time
# # a=time.time()
# a=time.localtime(2000)
# print(a)
# #a=time.strftime('%Y-%m-%d %H:%M:%S %w')
# a=time.strptime('2011-12-22 10:09:00','%Y-%m-%d %H:%M:%S')
# time.sleep(2)
# b=(2014,11,11,11,11,11,23,1111,1)
# a=time.mktime(b)
# print(a)
# import time
# a=input('请输入一个日期')
# print(a)
# b=time.strptime(a,'%Y-%m-%d')
# print(b)
# if b[0]%4==0:
#     print('是闰年')
# else:
#     print('不是闰年')
# if b[0]%400==0:
#     print('世纪闰年')
# else:
#     print('不是世纪闰年')
# print('是今年第{}天'.format(b[7]))
# print('是周{}'.format(b[6]+1))
# import os
# print(os.getcwd())
# os.chdir(r'C:\Users\zzq')
# print(os.getcwd())
# b=os.popen('ping 192.168.0.200')#执行cmd命令    命令必须是有结果的命令
# print(b.read())
# print(os.listdir())
# b=os.path.isdir(r'‪C:\Users\Public\Desktop\Xshell 5.lnk')
# print(b)
# a,b,c=os.ssh123.exec_command('ls -al /home')
#发送邮件
# import smtplib#封装了smtp协议
# import email.mime.multipart as mul#制作邮件
# import  email.mime.text as text#对邮件正文进行处理
# message=mul.MIMEMultipart()#创建空邮件
# message['Subject']='python_test'#标题命名
# message['From']='zzq981101@163.com'#发件人
# message['To']='348142851@qq.com'#收件人
# txt="""
# hello world
# 你好 中国
# """                             #正文
# tet=text.MIMEText(txt)        #对正文进行处理
# message.attach(tet)            #将处理过后的正文添加到邮件里
# att1=text.MIMEText(open('a.py','rb').read(),'base64','utf-8')#给邮件添加附件
# att1["Content-Type"]='application/octet-stream'
# att1["Content-Disposition"] = 'attachment; filename="a.py"'    #这里的filename可以任意写，写什么名字，邮件中显示什么名字
# message.attach(att1)            #定义一个邮件服务器
# smtp123=smtplib.SMTP_SSL('smtp.163.com',465)
# smtp123.login('zzq981101@163.com','123456zzq')#登录服务器   密码是授权码    不是邮箱密码
# smtp123.sendmail('zzq981101@163.com','348142851@qq.com',message.as_string())     #发送邮件   发件人  收件人  邮件
# smtp123.close()
#面试题
# import re
# a=input('请输入一组字符串')#vasv3q5jbj5b23j1233bkj2b675
# b=re.compile('[0-9][0-9]+')
# c=b.findall(a)
# print(c)
