import os,socket,subprocess,time,threading,urllib,wmi

from datetime import datetime
from queue import Queue
from bs4 import BeautifulSoup

def getIP():
    host=input('url/link: ')
    print (socket.gethostname(host))

def pingsweep():
    net  = input("target IP:")
    net1 = net.split('.')
    a='.'
    net2= net1[0]+a+net1[1]+a+net1[2]+a
    st1 = int(input("No awal: "))
    en1 = int(input("No akhir: "))
    en1 = en1+1
    t1  = datetime.now()
    print("executing x_x")
    for ip in range(st1,en1):
        address = net2+str(ip)
        res = subprocess.call(['ping',address])
        if res == 0: print("PING TO",address,"ok")

    t2 = datetime.now()
    total =t2-t1
    print(total)

def traceroute():
    ip= input("target IP:")
    results=os.popen('pathping'+str(ip))
    for i in results:print(i)

def tcpsweep():
    net=input("target IP: ")
    