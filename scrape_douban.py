import requests
from bs4 import BeautifulSoup
title=[]
author=[]
publisher = []
publish_date = []
description=[]
headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36"
}
for i in range(0,500,25):
	response = requests.get(f"https://book.douban.com/top250?start={i}",headers=headers)
	print(response.status_code)
	html = response.text
	soup = BeautifulSoup(html,"html.parser")
	items_1 = soup.findAll('div' ,class_='pl2')

	for i in items_1:
		tag=i.find("a")
		title.append(tag['title'])

	items_2 = soup.findAll("p",class_='pl')
	for k in items_2:
		description.append(k.string.split(" / "))
	for i in range(0,len(description)):
		author.append(description[0])
		publisher.append(description[1])
		publish_date.append(description[2])
print(description)
