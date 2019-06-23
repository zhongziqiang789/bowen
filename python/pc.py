import requests
import re
import json
import xlwt
import xlrd
url='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.89558461&x-zp-page-request-id=794f463973774a70b3d99ec14ed9ac49-1557276249061-413042%E8%AF%B7%E6%B1%82%E6%96%B9%E6%B3%95:GET'
reg=requests.get(url)
html=reg.content.decode("utf-8")
asd=json.loads(html)
a=[]
for i in range(0,90):
    b=asd['data']['results'][i]['company']['name'],asd['data']['results'][i]['jobName'],asd['data']['results'][i]['salary'],asd['data']['results'][i]['eduLevel']['name']
    a.append(b)
print(a)
ff=xlwt.Workbook(encoding='utf-8')
sheet=ff.add_sheet('zlzp')
c=['公司名称','公司职位','薪资','文凭']
for i in range(len(c)):S
    sheet.write(0,i,c[i])
for k in range(len(a)):
    for t in range(len(a[k])):
        sheet.write(k+1,t,a[k][t])
ff.save('zlzp.xls')

