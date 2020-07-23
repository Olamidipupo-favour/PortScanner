# -*- coding: utf-8 -*-
import socket
import datetime as t
info="""
===============!!!======!!=================|
|NAME:PORT SCANNER                         |
|AUTHOR:AGBOOLA OLAMIDIPUPO.               |
|EMAIL:dipoagboola2019@gmail.com.          |
|FACEBOOK:Olamidipupo favor.               |
|GITHUB:olamidipupo-favor.                 |
|WEBSITE:http://dipogeek.000webhostapp.com.| 
|©Agboola Olamidipupo 2020.                |
|DISCLAIMER:USE AT YOUR OWN RISK.          |
|============!!===!!!======================|
"""
print(info)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
hoste=str(input("HOST? => "))
rangeip=str(input("x-y? =>"))
p=rangeip.split('-')
time = t.datetime.now()
portl=[]
portno=[]
ports=[]
j=int(p[0])
k=int(p[1])
host=socket.gethostbyname(hoste)
print (f"[+] SCANNING HOST {host} WITHIN THE RANGE {j} AND {k}")
for i in range(j,k+1):
    try:
        j=s.connect((host, i))
    except:
        continue
    else:
        s.close()
        portl.append(i)
        continue 
time1=t.datetime.now()
print (f"[+] \a {host} SCANNED IN {time1-time} HOURS")
for i in ports:
    if(i not in portno):
        portl.append(i)
print ("------------------RESULTS-----------------")
for i in portl:
    print(f"{i} |  OPEN")
