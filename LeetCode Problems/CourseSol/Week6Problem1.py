import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if url == "":
    url = "http://py4e-data.dr-chuck.net/comments_1648076.json"
html = urllib.request.urlopen(url, context=ctx).read()

info = json.loads(html)

allcomments = info["comments"]
totalcomments =0
for countofcooments in allcomments:
    totalcomments += countofcooments["count"]
print(totalcomments)


