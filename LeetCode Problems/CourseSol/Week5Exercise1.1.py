import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
url = input("Enter -")
if url == "":
    url = "http://py4e-data.dr-chuck.net/comments_1648075.xml"
    html =urllib.request.urlopen(url).read()
commentinfo = ET.fromstring(html)
lst = commentinfo.findall("comments/comment/count")
countofcomment = commentinfo.findall(".//count")
counter = 0
for each in countofcomment:
    counter += int(each.text)
print(counter)
