#！/usr/bin/python
#-*-  coding:utf-8  -*-
#print('hello')
#a=input('请输入密码：')

#print(a)
#a=3
#b=4
#c=5
#print(a,b,c)
#a,b,c,d=3,4,"qwe",56
#print
#a="ewrq23dqwre"
#print(a[1::2])
#b=a.upper( )
#b=a.split("wr" )
#print(b)
#c="wr".join(b)
#print(c)
#abc=[1,2,4,8,10,5]
#b=[1,2,3]
#import  copy
# c=[4,5,6]
# a=[12,31,51,c,4543]
# print(type(a))
# ff=a.copy()
# c.append(100)
# a.append(20000)
# print(a)
# print(ff)
#
#a={"name":"小明","age":12}
#b={"p":123,"o":456}
#a={12,13,15,"wer"}
#b={12,31,24}
#c=a-b
#print(a-b)
#b=2
#a="user{}".format(b)
#print(a)
# a="user"
# b="qwe"
# print(a+b)
# a="user{}qwe{}asd{}"
# b=a.format(12,34,56)
# print(b)
# a="123"
# print(type(a))
# a=tuple(a)
# a = input(">>>")
# a=int(a)
# if  a > 3:
#   print("hello")
# a = 4
# if a > 3 or a > 10:
#     print("hello")
# elif a < 2:
#     print(123)
# elif a ==3:
#     print("900")
# else:
#     print(10000)
# a = input(">>>")
# a=int(a)
# if  a>=90:
#     print("优")
# elif  90>a>= 80:
#     print("良")
# elif  80>a>=70:
#     print("及格")
# else:
#     print("不及格")
# a = input(">>>")
# a = int(a)
# if  a%2==0:
#     if a%3==0:
#         print("hell0 world")
# if  a%2==0:
#     if  a%3!=0:
#         print("hello")
# if  a%2!=0:
#     if  a%3==0:
#         print("world")
# if   a%2!=0:
#     if  a%3!=0:
#         print(123)
#a = 12
#1+2+3+4+5....+100
# sum=0
# for  i  in  range(1,101):
#    sum=sum+i
# print(sum)
#1-2+3-4+5-6+7....-98+99=50
# sum=0
# for  i  in  range(1,100):
#     if  i%2==0:
#         sum=sum-i
#     else:
#         sum=sum+i
# print(sum)
#只不打印7
# for  i in  range(10):
#     if  i==7:
#         continue
#     print(i)
 #三次猜数字
 #1.猜对了就打印   恭喜  结束
 #2.如果猜的数字比随机产生的数字小，提示  小了
 #3.如果猜的数字比随机产生的数字大，提示  大了
# import  random
# a=random.randrange(1,4)
# for i in range(3):
#     b = input(">>>")
#     b = int(b)
#     if  a==b:
#         print("恭喜  结束")
#         break
#     elif b>a:
#         print("大了" "还有{}次机会".format(3-i))
#     else:
#         print("小了"  "还有{}次机会".format(3-i))
# else:
#     print("菜")
# a=[12,31,4]
# for  i,j  in  enumerate(a):
#     print(j)
#九九乘法表
# for i in range(1,10):
#     for  j  in  range(1,i+1):
#        print("{}*{}={}".format(j,i,i*j),end="\t")
#     if i==j:
#         print(" ")
#100以内的质数之和
# sum=0
# for i in range(2,101):
#     for  j  in  range(2,i+1):
#         a=i%j
#         if  a==0:
#            break
#     if  i==j:
#         sum=sum+i
# print(sum)
#因数之和等于它本身
# def  asd(a):
#     for i in range(1,a):
#         sum = 0
#         for j in range(1,i):
#             if i%j == 0:
#                 sum = sum + j
#         if sum == i:
#             print(i)
# asd(1000)
#水仙花数
# for i in range(100,1000):
#     x=i//100
#     y=i//10%10
#     z=i%10
#     if i==x**3+y**3+z**3:
#      print(i)
#阶乘之和
# a=input(">>>")
# a=int(a)
# b=0
# c=1
# for i in range(1,a+1):
#     c=i*c
#     b=b+c
# print(b)
#回文数
# a=input(">>>")
# if a==a[::-1]:
#    print("是回文数")
# else:
#    print("不是回文数")
#1+100的和
# sum=0
# i=0
# while  i < 100:
#     i=i+1
#     sum=sum+i
# print(sum)
#从键盘上输入若干个学生的成绩，统计平均成绩并输出低于平均分的学生成绩，用输入负数结束输入
# while  True:
#   a = input(">>>")
#   a = a.split(",")
#   for i,j in enumerate(a):
#     a[i] = int(j)
#   b = sum(a)//len(a)
#   if  a[0] < 0:
#       break
#   print("平均数为{}".format(b))
#   for k in  a:
#       if k < b:
#         print("低于平均数的有{}".format(k))
# while  True:
#     a = input(">>>")
#     a = a.split(",")
#     a = [int(i) for i in a]
#     b = sum(a)//len(a)
#     if  a[0] < 0:
#         break
#     print("平均数为{}".format(b))
#     d = [k for k  in a if k < b]
#     print(d)
#去重
# a = [12,1,21,23,13,12,12,12,13,23]
# a.sort()
# for  i  in  a:
#     b = a.count(i)
#     if b > 1:
#         for j in range(b-1):
#          a.remove(i)
# print(a)
#把九九乘法表放到a.txt文件中
# f = open(r"a‪.txt","w",encoding="utf-8")
# for i in range(1,10):
#     for j in  range(1,i+1):
#       f.write('{}*{}={}\t'.format(j,i,j*i))
#     f.write('\n')
# f.close()
# f = open(r"a‪.txt","r",encoding="utf-8")
# a=f.readlines()
# for i in a:
#     if  i[:3]=="abc":
#      print(i)
# f = open(r"a‪.txt","r",encoding="utf-8")
# for i in range(1,21):
#     if i < 15:
#      f.readline()
#     else:
#         b = f.readline()
#         print(b)
# for i in range(100,1001):
#     x=i//100
#     y=i//10%10
#     z=i%10
#     if i==x**3+y**3+z**3:
#      print(i)
#选择法排序
# a = input(">>>")
# b = a.split(",")
# b = [int(i) for i in b]
# c = len(b)
# for i in range(c):
#     for  j  in  range(i+1,c):
#         if b[i] > b[j]:
#             t=b[i]
#             b[i]=b[j]
#             b[j]=t
# print(b)
#冒泡法排序
# a = input(">>>")
# b = a.split(",")
# b = [int(i) for i in b]
# c = len(b)
# for  i  in range(1,c):
#     for j  in range(c-1):
#         if b[j] > b[j+1]:
#            t = b[j]
#            b[j] = b[j+1]
#            b[j+1] = t
# print(b)
#打印列表中所有的第一大数和第二大数
# a = input(">>>")
# b = a.split(",")
# b = [int(i) for i in b]
# b.sort()
# c = []
# d = b.count(b[-1])
# for i in range(1,d+1):
#     c.append(b[-1])
#     b.remove(b[-1])
# f = b.count(b[-1])
# for i in range(1,f+1):
#     c.append(b[-1])
# print(c)
# f = open("aa.jpg","rb")
# print(f.read( ))
# f.close()
# with  open("a.txt","r+",encoding="utf-8") as  f:
#     b = f.read()
#     f.write('wrre')
# def a():
#     b=0
#     for i in range(101):
#         b+=i
#     print(b)
# a()
#公鸡2块钱一只，母鸡1块钱一只，小鸡0.5块钱一只，100块钱可以买多少只公鸡，母鸡，小鸡
# for x in range(0,101):
#     for y in range(0,101):
#         z = 100-x-y
#         if 2*x+y+0.5*z==100:
#             print(x,y,z)
#任意4个数字，组成不相同的三位数
# a = input(">>>")
# b = a.split(",")
# b = [int(i) for i in b]
# for i in b:
#     for j in b:
#         for k in b:
#            if i!=j and j!=k and k!=i:
#                print(i,j,k)
# 判断三角形
# a = input('>>>')
# b = a.split(",")
# b = [int(i) for i in b]
# b.sort()
# if  b[0]+b[1] > b[2] and b[0]-b[1] < b[2]:
#         print("是三角形")
# else:
#         print("不是三角形")
#  变量的作用域
#  变量的分类：局部变量  全局变量
# b = 1
# def a():
#     global b
#     b = 0
#     print(b)
# a()
# print(b)
# 传参
# 参数名==变量名
# 定义函数：def  函数名(参数名):  执行语句块
#参数的个数是任意的
#必须参数：使用函数时必须要传入数据的参数
#默认参数：使用函数时可以传入数据也可以不传入数据
#可变长参数
#1.使用函数时可以传入数据也可以不传入数据
#2.使用函数时可以传入多个数据
#格式：def函数名（*参数名）：执行语句块
# def  asd(x):
#     a = sum(range(x+1))
#     print(a)
# asd(100)
# def  asd(p,b):
#     print(b)
# asd(b=12,p=13)
# def  asd(b=100):
#     a = 0
#     for  i  in  range(b+1):
#         a = a+i
#     print(a)
# asd(10)
# def  b(x,y):
#     sum = 0
#     for i in range(x,y+1):
#         for j in range(2,y+1):
#              if  i%j==0:
#                  break
#         if i==j:
#             sum= sum+i
#     print(sum)
# b(2,100)
# def  asd(a,b=10,*args):
#     print(a)
# asd(100)
#return
#1.结束函数    2.赋值
#第一步：1-任意数的和
#第二步：1-任意数的和+2，
# def  asd(b):
#     a = 0
#     for i in range(1,b+1):
#         a = a+i
#     return a
# def asd(x):
#     a = 0
#     for i in range(x+1):
#         a +=i
#     return  a
# print(asd)
# # asd(100)调用函数 = None
# # asd(100) = return 数据 = 数据
# for j in range(10,41,10):
#     c = asd(j)+2
#     h = asd(j)+2
#     i = asd(j)+2
#     l = asd(j)+2
#     print(c,h,i,l)
#计算器
# a = lambda x,y : x+y
# b = lambda x,y : x-y
# c = lambda x,y : x*y
# d = lambda x,y : x/y
# while True:
#    s = input(">>>")
#    if "-" in s:
#       q = s.split("-")
#       print(b(int(q[0]),int(q[1])))
#    elif "+" in s:
#        w = s.split("+")
#        print(a(int(w[0]),int(w[1])))
#    elif "*" in s:
#        e = s.split("*")
#        print(c(int(e[0]),int(e[1])))
#    elif "/" in s:
#        r = s.split("/")
#        print(d(int(r[0]),int(r[1])))
#    else:
#        break
# 自定义一个函数，给这个函数三个参数
# 第一个参数是字符串，第二个和第三个都是数字
# 删除这个字符串从第二个数字为下标位置，删除第三个数字
# def  a(x,y,z):
#     x = list(x)
#     d = y+z
#     if d > len(x):
#         d = len(x)
#     for i in range(y,d):
#         x.pop(y)
#     x = str(x)
#     b = " ".join(x)
#     print(b)
# a("asdfgh",2,7)
#将列表中的元素向左挪一位
# a = input(">>>")
# a = a.split(",")
# a = [int(i) for i in a]
# b = len(a)
# t = a[0]
# for i in range(len(a)-1):
#     a[i] = a[i+1]
# a[-1] = t
# print(a)
#一个有顺序的列表，随机加入一个数，加入的数在正确的位置
# import  random # 随机产生一个数
# a = random.randrange(10)
# a = int(a)
# b = [2,4,6,8]
# b.append(a)
# for i in range(len(b)):
#     for j in range(len(b)-1):
#         if b[j] > b[j+1]:
#             t = b[j]
#             b[j] = b[j+1]
#             b[j+1] = t
# print(b)
#十进制转换成十六进制
# a = int(input(">>>"))
# ff = [str(i) for i in range(10)]+["a","b","c","d","e","f"]
# c = " "
# while True:
#     b = a % 16
#     c = c + ff[b]
#     a = a // 16
#     if a == 0:
#         break
# print(c[::-1])
#购物车
# num = eval(input("请输入总资产"))
# goods= [
#     {"name":"电脑","price":1999},
#     {"name":"鼠标","price":10},
#     {"name":"游艇","price":20},
#     {"name":"美女","price":998},
# ]
# print("请输入要购买的商品")
# print("0:电脑\n1:鼠标\n2:游艇\n3:美女\n")
# num_goods=eval(input('请输入序号：'))
# sum = 0
# if type(num_goods,int):
#     sum = sum+goods[num_goods]["price"]
# else:
#     for isinstance(num_goods,int):
#         sum +=goods[num_goods]["price"]
# else:
#     for i in range(len(num_goods)):
#         if num_goods[i] > 4:
#              print("")
#
# num = eval(input('请输入金额：'))  # 只能输入数字
# goods = [
#     {'name': "电脑", 'price': 1999},
#     {'name': "鼠标", 'price': 10},
#     {'name': "游艇", 'price': 20},
#     {'name': "美女", 'price': 998},
# ]
# print('请输入要购买的商品：')
# print('0：电脑\n1：鼠标\n2：游艇\n3：美女')
# num_goods = eval(input('请输入序号：'))  # 只能输入多个，输入多个时中间用逗号隔开
# sum = 0
# if isinstance(num_goods, int):
#     sum += goods[num_goods]['price']
# else:
#     for i in range(len(num_goods)):
#         if num_goods[i] > 4:
#             print('请输入0~3中的数字，该商品无效，已删除')
#         else:
#             sum += goods[num_goods[i]]['price']
# if num > sum:
#     flag = input('确认购物吗？，请输入y or n：')
#     if flag == 'y':
#         remained = num - sum
#         print('购物成功！剩余金钱为:', remained)
#     else:
#         print('请继续购物或删除商品！')
# else:
#     while (num < sum):
#         chongzhi = eval(input('您的余额不足！请充值：'))
#         num = chongzhi + num
#         print('充值成功！')
#     flag = input('确认购物吗？，请输入y or n：')
#     if flag == 'y':
#         remained = num - sum
#         print('购物成功！剩余金钱为:', remained)
# a = input(">>>")
# a = int(a)
# sum = 0
# for i in range(2,1001):
#     for j in range(1,1000):
#         a = i%j
#         if a == 0:
#             sum = sum+j
#     if sum == i:
#         print(sum)
#导入 语句
#import  语句
#1.import  文件名
#2.from  文件名  import  函数名
# def asd():
#     print("hello")
# asd()
# def qwe():
#     print(123)
# qwe()
# # 判断正在执行的文件，是否是本文件
# #如果是:执行判断语句下的语句
# if  __name__ == '__main__':
#     for i in range(10):
#         print(i)
# with  open('a.txt','r',encoding='utf-8') as f:
# #     b = f.readline()
# #     c = []
# #     for i in range(len(b)):
# #         b = b[i]
# #         b = b.split(',')
# #         c.append(b)
#九九乘法变写入excel中
# import xlwt
# f = xlwt.Workbook(encoding='utf-8')
# sheet = f.add_sheet('python_test')
# for i in range(1,10):
#     for j in range(1,i+1):
#         sum = '{}*{}={}'
#         num = sum.format(i,j,i*j)
#         if i == j:
#             print('')
#         sheet.write(i-1,j-1,num)
# f.save('aaa.xls')
# import  xlrd
# f = xlrd.open_workbook("aaa.xls")
# sh = f.sheets.()[0]
# sum = sh.nrows
# num = sh.ncols
# new_f = copy(f)
# sheet = new_f.get_sheet(0)
# for i in range(10):
#     sheet.write(num+i,0,"qwe")
# new_f.save("aaa.xls")


#创建数据库
# import  pymysql
# conn = pymysql.connect(host="192.168.0.111",port=3306,user="root",passwd="123456")
#创建游标
# m = conn.cursor()
#执行sql语句  显示数据库的个数
# m.execute("create database  python_learn;")
# m.execute("use python_learn;")
#m.execute("create table biao(name char(20),age int,sex char(20));")
#m.execute('insert into biao value("小红",20,"女"),("小华",18,"男");')
# m.execute('select * from biao;')
# m.execute("show databases")
# print(m.fetchall())
#m.execute("show tables;")
#读取上一个sql语句的结果  结果是个元组
# b = m.fetchall()
#默认一次只读取一个数据
#传入的参数是数字几就读取几条数据
#b = m.fetchmany()
#每次只读取一条数据
# # #b = m.fetchone()
# # # print(b)
#断开数据库
# conn.close()


# import  pymysql
# conn = pymysql.connect(host="192.168.0.111",port=3306,user="root",passwd="123456")
# m = conn.cursor()
# m.execute("use python_learn;")
# for i in range(30):
#     m.execute('insert into biao value("小红",{},"女");'.format(i))
# m.execute('drop table biao;')
# b = m.fetchall()
# print(b)
# conn.close()

# import pymysql
# import  xrld
# conn = pymysql.connect(host="192.168.0.111",port=3306,user="root",passwd="123456")
# m = conn.cursor()
# m.execute("use python_learn;")
# sheet = f.sheets()[0]
# for i in range(sheet.nrows):
#     b = sheet.row_values(i)
#     if i==0:
#         continue
#         m.execute('create table zhilian({} char(255),{} char(255),{} char(255),{} char(255),{} char(255),{} char(255),{} char (255);'.format(b[0],b[1],b[2],b[3],b[4],b[5],b[6]))
#     else:
#         m.execute('insert into zhilian values("{}","{}","{}","{}","{}","{}","{};".format(b[0],b[1],b[2],b[3],b[4],b[5],b[6]))
# m.execute("select * from zhilian;")
# c = m.fetchall()
# print(c)


#将excel文件写入数据库中
# import  pymysql
# import  xlrd
# f = xlrd.open_workbook("aaa.xls")
# conn = pymysql.connect(host="192.168.0.111",port=3306,user="root",passwd="123456")
# m = conn.cursor()
# m.execute("use python_learn;")
# sheet = f.sheets()[0]
# for i in range(sheet.nrows):
#     b = sheet.row_values(i)
#     if i==0:
#         #continue
#         m.execute('create table zhilian({} char(255),{} char(255),{} int ,{} int);'.format(b[0],b[1],b[2],b[3]))
#     else:
#         m.execute('insert into zhilian values("{}","{}","{}","{}");'.format(b[0],b[1],b[2],b[3]))
# m.execute("select * from zhilian;")
# c = m.fetchall()
# print(c)

#将a.txt文件导入到数据库中
# import pymysql
# f = open('a.txt','r',encoding='utf-8')
# a = f.readlines()
# conn = pymysql.connect(host="192.168.0.111",port=3306,user="root",passwd="123456")
# m = conn.cursor()
# m.execute("use python_learn;")
# for i in range(len(a)):
#       c = a[i].split(",")
#       print(c)
#     if i == 0:
#         m.execute('create  table chenji({} char(255),{} char(255),{} int ,{} int);'.format(b[0],b[1],b[2],b[3]))
#     else:
#         m.execute('insert into chenji values("{}","{}","{}","{}");'.format(b[0], b[1], b[2], b[3]))
# m.execute("drop table  chengji;")
# c = m.fetchall()
# print(c)


# 将文件从mysql数据库导入到aaa.xls
# import pymysql
# import  xlwt
# conn = pymysql.connect(host="192.168.0.111",port=3306,user="root",passwd="123456")
# m = conn.cursor()
# m.execute("use python_learn;")
# m.execute('desc chenji;')
# a = m.fetchall()
# print(a)
# f = xlwt.Workbook(encoding='utf-8')
# sheet = f.add_sheet('python')
# c = []
# for i in range(len(a)):
#     c.append(a[i][0])
#     sheet.write(0,i,c[i])
# m.execute('select * from chenji;')
# b = m.fetchall()
# for j in range(len(b)):
#     for k in range(len(b)):
#         sheet.write(j+1,k,b[j][k])
# f.save('aaa.xls')

#将mysql数据库中的表导入到txt文件中



#python与操作系统交互的模块
# import  os
# import pymysql
# import  xlwt
# conn = pymysql.connect(host="192.168.0.111",port=3306,user="root",passwd="123456")
# m = conn.cursor()
# m.execute("use python_learn;")
# m.execute('desc chenji;')
# a = m.fetchall()
# m.execute('select * from chenji;')
# c=m.fetchall()
# print(c)
# y=li# print(type(y))
# # print(y)st(c[0])

# b = []
# for j in range(len(a)):
#     b.append(a[j][0])
# x=','.join(b)
# print(x)
# with open("a.txt","w",encoding="utf-8")as f:
#     for i in range(len(c)):
#         n = list(c[i])
#         z=','.join(n)
#         if i==0:
#             f.write(x)
#             f.write('\n')
#             f.write(z)
#             f.write('\n')
#         else:
#             f.write(z)
#             f.write('\n')








#获取当前所在的位置
# print(os.getcwd())
#切换目录
# os.chdir(r'E:\PycharmProjects\untitled1')
# print(os.getcwd())
#执行cmd命令,有结果的命令
# b = os.popen('ping 192.168.0.111')
# print(b.read())
#查看所有文件
#默认是查看当前目录下的
#传入参数
# print(os.listdir())
#创建目录
# os.mkdir('aaa')
#删除空目录
# os.rmdir('aaa')
#创建递归目录
# os.makedirs(r'aaa\bbb\ccc')
#删除递归目录
# os.removedirs(r'aaa\bbb\ccc')
#将路径与文件分隔开
# b = os.path.split(r'‪C:\Users\hyj\Desktop\百度网盘.lnk')
# print(b)
#将后缀名与路径分隔开
# b = os.path.splitext(r'‪C:\Users\hyj\Desktop\Mysql_整理(1).docx  答案.txt')
# print(b)
#判断是否是普通文件
# b = os.path.isfile(r'‪E:\软件测试工程师实训大纲V4.0 (1).xlsx')
# print(b)
#判断是否是目录
# b = os.path.isdir(r'‪E:\360downloads')
# print(b)
#删除文件
# os.remove('a.txt')

#将本目录下的所有.py的文件打印出来
# import os
# a = os.listdir()
# for i in a:
#     b = os.path.isfile(i)
#     c = os.path.splitext(i)
#     print(c)
#     if  b == True:
#         if c[1]=='.py':
#             print(i)
# import  os
# a = os.listdir()
# for i in a:
#     a = str(i)
#     b = a.endswith('.py')
#     print(b)
#     if b == True:
#         print(i)


#封装了ssh协议，可以实现远程控制
# import  paramiko
#创建一个ssh客户端
# ssh123 = paramiko.SSHClient()
# with paramiko.SSHClient() as ssh123:
#跳过从know_hosts文件中验证
  #   ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接主机
#     ssh123.connect(hostname="192.168.0.111",port=22,username="root",password="123456")
# #执行命令
#第一个变量:标准输入的命令,必须是有结果的命令
#第二个变量:命令的输出
#第三个变量:命令的报
    # a,b,c = ssh123.exec_command("ls  -al  /home")
    # print(b.read().decode())
#断开连接
# ssh123.close()

# import  paramiko
# ssh123 = paramiko.SSHClient()
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh123.connect(hostname="192.168.0.111",port=22,username="root",password="123456"
# a,b,c = ssh123.exec_command("ls  -al  /home")
# print(b.read().decode())

#上传和下载文件
# import  paramiko
#创建一个传输通道
# qq = paramiko.Transport(("192.168.0.111",22))
#连接
# qq.connect(username="root",password="123456")
#使用ssh协议创建一个传输文件的功能
# sftp = paramiko.SFTPClient.from_transport(qq)
#下载文件，从linux上传文件到windows
# sftp.get("/home/test.sh","b.sh")
#上传文件，从windows上传文件到linux
# sftp.put("hyj1.py","/etc/hyj1.py")
#
# 发送邮件   smtp，pop3  imap
# import  smtplib  #封装了smtp协议
# #制作邮件
# import  email.mime.multipart  as  mul
# #对邮件的正文进行处理
# import  email.mime.text as  text
# #给发件人赋变量
# ff = 'hyjie_2018@163.com'
# # 给收件人赋变量
# ww = ["2595271431@qq.com","hyjie_2018@sina.com"]
# #创建一个空邮件
# message = mul.MIMEMultipart()
# #标题
# message['Subject'] = 'python_test'
# #发件人
# message['From'] = 'hyjie_2018@163.com'
# #收件人
# # message['To'] = '2595271431@qq.com'
# message['To'] = '.'.join(ww)
# #正文   多行数据
# txt = """
# 中国
# 河南
# 开封
# """
# #对正文进行处理
# tet = text.MIMEText(txt)
# #将处理过后的正文添加到邮件里
# message.attach(tet)
#
# #带有附件的邮件
# att1 = text.MIMEText(open('hyj1.py', 'rb').read(), 'base64', 'utf-8')
# #附件的字段   固定的
# att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="b.py"'
# message.attach(att1)
#
# # 定义邮件服务器
# smtp123 = smtplib.SMTP_SSL('smtp.163.com',465)
# #登录服务器   用户名，密码(不是邮箱密码是授权码)
# smtp123.login('hyjie_2018@163.com','jie2121')
# #发送邮件   发件人   收件人   邮件
# smtp123.sendmail(ff,ww,message.as_string())
# #断开连接
# smtp123.close()

#套接字，提供了通信双方最底层的功能（发送，接收）
# socket
#C/S架构，通过socket实现基本的通信

#server端  服务器：可以提供某种服务的产品，软件
# import  socket
#创建一个套接字（具有发送和接收能力）
#SOCK_STREAM  指的是tcp
#AF_INET   指的是IPv4
# import  socket
# s =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定IP
# s.bind(('192.168.0.36',3000))
#监听
# s.listen(3)   #3：是当达到处理极限时，最大等待个数
# while True:
    #接收客户端建立的连接
    #接收的是建立连接
#     #第一个变量的结果是：建立连接的信息
#     #第二个结果：客户端的Ip和端口号
#     # client,addr = s.accept()
#     # print(client)
# #接收客户端发送的数据
#     #1024指的是每次接受的最大数据  B
#     # reg = client.recv(1024)
#     # print(reg.decode('utf-8'))
#     #发送的数据
#     # msg = input(">>>")
#     #给客户端发送响应
#     # client.send(msg.encode('utf-8'))

# def  asd(a,b):
#     for i in range(len(a)):
#         for j in range(len(a)):
#              if  a[i] + a[j] == b:
#                  print(a[i],a[j])
# asd([11,11,3,2,20,4,5,10],22)

#创建一个套接字
# import  socket
# #IPv4，SOCK_DGRAM   UDP
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #绑定IP地址
# s.bind(('192.168.0.36',3000))
# while  True:
#     #接收客户端的请求
#     #第一个变量：是客户端的请求数据
#     #第二个变量：是客户端的IP和端口号
#     client,addr = s.recvfrom(1024)
#     print(client.decode('utf-8'))
#     #发送响应
#     msg = input(">>>")
#     s.sendto(msg.encode('utf-8'),addr)

#正则表达式
#匹配文件中的字符串
# with  open('a.txt','r') as f:
#     a = f.read()
# print(a)
#匹配a中的数字
#自己写的正则表达式对于python来说，python是不认识的
#需要将正则表达式转换成python能够识别的正则表达式
# import  re
#将字符串转换成正则表达式
# a = 'wert123asd789'
#将正则表达式编译成python能够识别的正则语言
# b = re.compile('123(.*)789')
#拿着编译之后的正则到字符串中去查找
#查找所有符合条件的字符，结果是一个列表
#findall除了查找，本身就具有编译的能力
# c = b.findall(a)
# print(c)
#贪婪模式：尽可能多的去匹配符合条件的内容
#非贪婪模式：尽可能少的去匹配符合条件的内容（?）
# import  re
# with  open('a.txt','r') as f:
#      a = f.read()
# .匹配任意一个字符，除了换行符之外的
# 给 . 加上拥有匹配换行符在内的功能  re.S
# 正则表达式区分大小写，加上  re.I  让正则表达式不区分大小写
# a = ['wer654436532456456tasddsdvfw','441515','5454']
# b = re.compile('W(.*)w',re.I)
#findall除了查找，本身就具有编译的能力
# c = re.findall("w(.*)w",a)
#替换，将字符串中的某些字符替换为其他的
# for i in a:
    #第一个参数：通过正则过滤出被替换的字符
    #第二个参数：替换成的字符
    #第三个参数：要被替换的字符串c
    # c = re.sub('[0-9]+','abc',i)
    # print(c)

# def  asd(a):
#     a = a.split(",")
#     a = [int(i) for i in a]
#     b = [j for j in b]
#     b.sort()

#python的函数
#10进制转16进制
# print(hex(123))
#10进制转8进制
# print(oct(123))
# #10进制转2进制
# print(bin(123))
# #任何进制转10进制
# print(int(0x172))

#chr将数字转化为asill表中对应的字符
# a = [chr(i) for i in range(97,103)]
# print(a)
# a = ['a','b','c']
# print(chr(97))
#ord将asill表中的字符转换成对应的数字
# print(ord('a'))

# a = [123,1,4,3215]
#求最大数
# print(max(a))
#求最小数
# print(min(a))
#求和
# print(sum(a))
#整数求余
# a,b = divmod(100,16)
# print(a,b)

#面向对象
# #将函数进行分类和封装，使开发更高效
# from  hyj1  import  *
# 1. 定义一个类   class  类名：
#  属性，方法（函数）
#  默认首字母大写
#调用   类名().函数名()
#  self不是函数的参数，self是类的实例，是方便在类的内部调用其他函数
#  继承：
# 括号中是写要继承的类
# 新的类会继承旧的类中的所有函数
# 多继承
# class  Ad():
#     def  asd(self):
#         a = 0
#         for  i in range(101):
#             a += i
#         print(a)
#         self.abc()
#     def  abc(self):
#         print(123)
# Ad().asd()
# class  Qwe():
#     def we(self):
#         print('456')
# class  Ji(Qwe):
#     pass
# q = Ji()
# q.we()

# class Yinshu():
#     def  asd(self,a):
#         for i in range(1,a):
#             sum = 0
#             for j in range(1,i):
#                 if i%j == 0:
#                     sum = sum + j
#             if sum == i:
#                 print(i)
#将类名()赋值给了一个对象
# ad = Ad()
# ad叫   类的实例(对象)  是方便在类的外部调用其他函数
# ad.asd()
# yinshu = Yinshu()
# yinshu.asd()
#
# class  Ab():
#     def yy(self):
#         print(123)
#     def rr(self):
#         print(789)
# class  Cd(Ab):
#     def __uu(self):
#         print(456)
#     def yy(self):
#         self.__uu()
#         print(123)
#         print('hello')
# class  Ef(Cd):
#     pass
# q = Cd()
# q.yy()
# 多态（方法重写）
# 继承的类中某个函数不满足需求，本类中自定义一个跟继承的类中函数名相同的函数
# 私有方法（函数）
# 不可被继承的，不能在类的外部调用的
# 只能在内部被调用
#  在函数名左边加两个下划线
#类的专有方法
#函数名左右有两个下划线的，专用方法是python内部固定的
#只要是个类，具有所有的专有方法
# 专有方法是不需要调用，会自动执行的
# 属性：一个类中所有的函数都具有的特点
# 基础值
# class  asd():
#     def __init__(self,name,xuelian):    #初始化属性
#         self.name= name
#         self.xuelian = xuelian
#     def daguai(self):
#         self.xuelian -= 200
#         print('{},还剩下{}'.format(self.name,self.xuelian))
#     def jiaxue(self):
#         self.xuelian += 500
#         print('{},还剩下{}'.format(self.name,self.xuelian))
#     def __repr__(self):   #输出
#         return  '{}'.format(self.a + self.b)
# q = asd("诸葛亮",1000)
# q.daguai()
# q.jiaxue()

# 面向对象
#优点：可扩展，易维护，可重复使用
#缺点：性能不好
# 面向过程：通过代码和逻辑一步一步实现要达到的目的
#优点：性能好
#缺点：不易维护，不可重复使用

#爬虫：模仿浏览器，根据自己制定的规则批量下载指定的资源
#分类：聚焦爬虫，搜索爬虫
#聚焦爬虫：只针对某个网站进行爬取
#搜索爬虫：针对全网络进行爬虫（搜索引擎）
#模仿浏览器：requests，urllib，urllib2,3
#过滤网页资源：re，Beautifulsoup，xpath
#爬虫第一步：分析网址
#爬虫第二步：找到想要的资源并过滤
#爬虫第三步：保存
#对服务器进行请求，将得到的响应数据过滤并保存
#反爬：防止爬虫程序，批量下载资源
#常见的反爬机制：
#  1.通过请求headers判断
#  2.IP地址被封    频繁的转换公网ip（西刺代理）
#  3.验证码
#  4.数据混淆
#  5.行为分析
#  爬虫本身不违法，做商业活动就违法了
# import  requests
# import  re
# title=[]
# class  FreeBuf():
#     def send_request(self):
#         url = 'https://www.freebuf.com/page/1'
#         # 发送请求
#         head = {
#             'User - Agent':'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 71.0.3578.98Safari / 537.36'
#         }
#         res = requests.post(url,headers=head)
#         # 读取结果  1.text  以文本的方式接收,结果是个字符串
#         # content  以字节方式接收
#         hh = res.content.decode('utf-8')
#         return  hh
#     def  guolv(self,x):
#         #二次过滤
#         patt = re.compile('<div class="news-info">(.*?)<dd>',re.S)
#         itesms = patt.findall(x)
#         for i in itesms:
#             aa = re.findall('title="(.*?)"',i)
#             title.append(aa[0])
#         return  title
#     def save(self,y):
#         with open('a.txt','a',encoding='utf-8') as f:
#             for i in y:
#                 f.write(i+'\n')
# fr = FreeBuf()
# for i in range(1,5):
#     hh = fr.send_request()
#     yy = fr.guolv(hh)
#     fr.save(yy)
# print(title)

#保存图片
# import  requests
# import  re
# class  qiu():
#     url = 'https://www.qiushibaike.com/imgrank/page/1'
#     head = {
#             'User - Agent':'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 71.0.3578.98Safari / 537.36'
#     }
#     res = requests.get(url,headers=head)
#     html= res.content.decode('utf-8')
# #过滤
#     patt = re.compile(r'<img src="//pic.qiushibaike.com/system/pictures/(.*?).jpg"')
#     items = patt.findall(html)
#     # a = 0
#     for  i  in  items:
#         j = 'https://pic.qiushibaike.com/system/pictures/'+i+'.jpg'
#         print(j)
    #     # 保存图片   先对图片链接请求，以字节的方式读取，以字节的形式保存
    #     msg = requests.get(j,headers=head)
    #     hh = msg.content
    #     with  open('{}.jpg'.format(a),'wb') as f:
    #         f.write(hh)
    #     a =+ 1

# import  requests
# import  re
# class  douban():
#     def send_request(self):
#         url = 'https://movie.douban.com/top250?qq-pf-to=pcqq.group'
#         head = {
#                     'User - Agent':'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/71.0.3578.98Safari/537.36'
#                 }
#         res = requests.post(url,headers=head)
#         html= res.content.decode('utf-8')
# fr = douban()
# h=fr.send_request()
# print(h)


#网页：静态网页 ：所有的资源都在html文件上
#      动态网页：资源不在html文件上
#  ajax（XHR）     javascript（js）
# Json：是一种轻量级的数据传输格式
# import  requests
# url = ''
# res = requests.get(url)
# hhh = res.content.decode('utf-8')
# #将字符串格式转化字典
# qqq = json.loads(hhh)
# print(qqq['data']['results'][1]['company']['name'])
# #将字典转换为字符串
# uuu = json.dumps(qqq)
# print(type(uuu))

#  zip    将多个列表一一对应
# a = [12,123,1314]
# b = ['a','b','c']
# aaa = zip(a,b)
# print(list(aaa))


# import requests
# import re
# class FreeBuf():
#     def send_request(self,c):
#         url ="https://www.freebuf.com/page/{}".format(c)
#         head={"user_agent":"Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko"}
#         #发送请求
#         res = requests.post(url,headers=head)
#         #读取结果1.text 以文本的方式接收结果是字符串 2.content 是以字节的方式接收，结果是字节的类型
#         hh=res.content.decode("utf-8")
#         return hh
#
#     def guolv(self,x):
#         patt=re.compile('<div class="news-info">(.*?)<dd>',re.S)
#         itesms=patt.findall(x)
#         title=[]
#         for i in itesms:
#             aa=re.findall('title="(.*?)"',i)
#             # print(aa)
#             title.append(aa[0])
#         return title
#     def save(self,y):
#         with open("e.txt","a",encoding="utf-8")as f:
#             for i in y:
#                 f.write(i+"\n")
#
# fr =FreeBuf()
# for i in range(1,5):
#     # fr.send_request()
#     xx=fr.send_request(i)
#     yy=fr.guolv(xx)
#     fr.save(yy)



# import requests
# import re
# url = 'https://www.qiushibaike.com/imgrank//page/2'
# head = {
#          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,likeGecko) Chrome/73.0.3683.103 Safari/537.36'
#         }
# res = requests.get(url,headers = head)
# html = res.content.decode('utf-8')
# patt = re.compile(r'<img src="//pic.qiushibaike.com/system/pictures/(.*?).jpg"')#(过滤)
# itesms = patt.findall(html)
# # print(len(itesms))
# a=0
# for i in itesms:
#     j = 'https://pic.qiushibaike.com/system/pictures/'+i+'.jpg'
#     # print(j)
#     #保存图片 先对图片的连接请求，以字节的方式读取，以字节的方式保存
#     msg=requests.get(j,headers=head)
#     hh=msg.content
#     with open('{}.jpg'.format(a),"wb",)as f:
#         f.write(hh)
#     a=a+1


# import requests
# import re
#
# url = "https://movie.douban.com/top250?ADUIN=1004745584&ADSESSION=1556523569&ADTAG=CLIENT.QQ.5611_.0&ADPUBNO=26885"
# res = requests.get(url)
# html = res.content.decode("utf-8")
# a = re.compile(
#     '<img width="100" alt="(.*)" src="https://img(.).doubanio.com/view/photo/s_ratio_poster/public/(.*).jpg" class="">')
# b = a.findall(html)
# print(b)
#
#
# for i in b:
#     print(i)
#     j="https://img{}.doubanio.com/view/photo/s_ratio_poster/public/{}.jpg".format(i[1],i[2])
#
#     print(j)
#     msg=requests.get(j)
#     hh=msg.content
#     f=open("{}.jpg".format(i[0]),"wb")
#     f.write(hh)
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind('192.168.0.80',3000)
s.listen(3)
while True:
    client,addr=s.accept()
    reg=client.recv(1024)
    print(reg.decode('utf-8'))
    qq=input='>>>'
    client.send(qq.encode('utf-8'))
