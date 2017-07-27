#-*- coding:CP949 -*-
import pymysql
from bs4 import BeautifulSoup
import os
import sys
import requests
import pymysql

conn=pymysql.connect(host='localhost',user='root',password='12137522',db='ip', charset='utf8')
'''if conn<=0:
    print("not connected")
    exit()'''
curs = conn.cursor()
sql="""insert into ip(snum,time,name,bank,acnt,ip,cntry) values (%s,%s,%s,%s,%s,%s,%s)"""
    
r=requests.get("http://fl0ckfl0ck.info")

soup=BeautifulSoup(r.text, 'html.parser')
timelist=[]
obj=soup.find_all('td',{'align':"right"})
num=0;
k=0;
s_time=[]
for i in range(0,2094*2,2):
    time = str(obj[i])
    s_time.append(time[18:22]+time[23:25]+time[26:28]+time[29:31]+time[32:34])
for (path,dir,files) in os.walk("./ips"):
    for filename in files:
        s_ip=path
        ip_count = s_ip.find("/ips/")
        s_ip = s_ip[ip_count+5:]
        ext=os.path.splitext(filename)[-1]
        f=open(path+"/"+filename,'r', encoding='euc-kr')
        data = f.read()
        print("nono")           
        tmp = data.split(',')
        tmp2=tmp[0]
        ttmp=tmp2.split('()')
        s_name=ttmp[0]
        s_name=s_name[3:]
        s_acnt=str(ttmp[1:2])
        s_acnt=s_acnt[2:-2]
        s_acnt=int(s_acnt)
        s_bank=str(tmp[1:2])
        s_bank=s_bank[5:-2]
        s_cnt=str(tmp[4:5])
        s_cnt=s_cnt[4:-2]
            
        num=num+1
        r = curs.execute(sql,(num,s_time[num-1],s_name,s_bank,s_acnt,s_ip,s_cnt))
        conn.commit()
conn.close()


