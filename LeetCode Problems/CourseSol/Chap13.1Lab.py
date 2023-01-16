"""
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times.
The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
"""
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
url = input("Enter url:")
count = int(input("Enter count :"))
pos = int(input("Enter Pos :"))
urllist = list()
for i in range(count):
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,"html.parser")
    tags = soup("a")
    #print("Retriving URL:",url)
    taglist = list()
    for tag in tags:
        y = tag.get("href",None)
        taglist.append(y)
    url = taglist[pos]
    urllist.append(url)
print("Last Url:",urllist[-2])

