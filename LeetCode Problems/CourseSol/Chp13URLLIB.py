import urllib.request, urllib.request

from bs4 import BeautifulSoup

x = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
print(x,"----",type(x))
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    #print(data.decode())
mysock.close()

html = urllib.request.urlopen("http://www.youtube.com").read()
soup = BeautifulSoup(html, 'html.parser')
x = soup('a')
print(x)
