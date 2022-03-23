import requests
from bs4 import BeautifulSoup
import re

#save the URLs for the Pudding Movie Dialogue article to a variable
with open ('/Users/zhangkaixin/Desktop/cornell movie-dialogs corpus/raw_script_urls.txt', 'r', encoding = "ISO-8859-1") as f:
    contents = BeautifulSoup(f, 'lxml')
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',contents.body.p.getText())  

#get the texts from the urls
#create a new file
f = open("scripts.txt", "w")
f.close()

f = open("scripts.txt", "a")

#use loop to save the text(scripts) into the file
for url in urls:
    response = requests.get(url)
    if (response.status_code != 404):
        script = response.text
        f.write(script)
f.close()
f = open("scripts.txt", "r")
print(f.read())
