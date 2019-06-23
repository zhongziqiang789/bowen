#range   范围函数  跟数字连用
#函数传参    传参：传递参数  灵活代码
#优先级     必须参数>默认参数>可变长参数
#
#只要索引出来的值              就可以继续索引
# import xlrd
# from xlutils.copy import copy
# f=xlrd.open_workbook('1111111.xls')
# sh=f.sheets()[0]
# num=sh.nrows
# nnn=sh.ncols
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# for i in range(10):
#     sheet.write(num+i,0,'qwe')
# new_f.save('1111111.xls')
#return     结束函数      给函数的调用者赋值
# def asd(x):
#         a=0
#         for i in range(50,x+1):
#             a+=i
#         return a
# #在之后的代码中需要用到此函数的结果
# print(asd(100))
#深复制   浅复制
#浅复制     只复制第一层数据  深层的数据是共用的
# a=[12,31,[111,23],3]
# b=a.copy()
# a[2].append(100)
# print(b)
# print(a)#深层的数据是共用的
#深复制
# import copy
# a=[12,31,[111,23],3]
# b=copy.deepcopy(a)
# a[2].append(100)
# print(b)
# print(a)
# import xlrd
# f=xlrd.open_workbook(r'1.xls')
# sheet=f.sheets()[0]
# b=f.nsheets
# print(b)
# sheet=f.sheets()[0]
# sheet1=f.sheets()[1]
# b=f.sheet_names()
# print(b)
# sheet=f.sheet_by_name('python_test')
# b=sheet.row_values(1)
# b=sheet.nrows
# for i in range(b):
#     c=sheet.row_values(i)
#     print(c)
# c=sheet.col_values(0)
# b=sheet.ncols
# print(b)
# c=sheet.col_values(0)
# print(c)
# import xlwt
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('python_test')
# for i in range(100):
#     sheet.write(i,0,i+1)
# f.save('1a.xls')
# from xlutils.copy import copy
# import xlrd
# f=xlrd.open_workbook('1.xls')
# sheet1=f.sheets()[0]
# b=sheet1.nrows
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# sheet.write(0,2,'111')
# new_f.save('1a.xls')
# class As():
#     def asd(self):
#         print('hello')
#
#
#     def qwe(self):
#         print(123)
#
# class Zx():
#     def dd(self):
#         print('hello world')
# class xy(As,Zx):
#     def ff(self):
#         print('hero is never die')


