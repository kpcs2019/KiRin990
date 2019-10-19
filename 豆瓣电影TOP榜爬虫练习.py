import requests
from bs4 import BeautifulSoup

user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;)"
headers = {"User-Agent":user_agent}
url = "https://movie.douban.com/top250?start="
for i in range(0,3):
	fullurl = url + str(i*25)
	res = requests.get(fullurl,headers=headers)
	soup = BeautifulSoup(res.text,"lxml")
	mlist = soup.find_all('div',{'class':'info'})
	j = 0
	for m in mlist:
		j += 1
		title = m.find('a').find('span').text
		score = '评分：' + m.find('div',class_='star').find('span',class_='rating_num').text + '分'
		link = '链接：' + m.find('a')['href']
		content = '片名：' + str((i*25) + j) + '-' + title + '\n' + score + '\n' + link + '\n'
		print(content)
print("======豆瓣电影TOP250数据爬取分析完毕======")
