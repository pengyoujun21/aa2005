"""
 接收浏览器访问，打印浏览器的头部信息
"""
import re
import sys
from socket import *

s = socket()
s.bind(("0.0.0.0",9999))
s.listen(5)

f = open("index.html","rb")
str = f.read()
f.close()
while True:
    confd,addr = s.accept()
    print("connect from :",addr)
    data  = confd.recv(4096)

    # result = re.match("[A-Z]+\s+(?P<info>/\S*)",data.decode())
    # print(result.group('info'))
    # sys.exit("---")
    print(data.decode())
    html = "HTTP/1.1 200 OK\r\n"
    html += "Content-Type:text/html; charset=utf-8"
    html += "\r\n"
    html = html.encode()+str
    confd.send(html)

    confd.close()
s.close()