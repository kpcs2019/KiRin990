import requests
from bs4 import BeautifulSoup

user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;)"
headers = {"User-Agent":user_agent}
url = "https://so.gushiwen.org/gushi/tangshi.aspx"
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")
shiwen = soup.find_all('div',{'class':'typecont'})
j = 0
weblinks = []

for i in shiwen:
	sp = i.find_all('span')
	for links in sp:
		j += 1
		link = 'https://so.gushiwen.org' + links.find('a')['href']
		name = links.find('a').text
		weblinks.append(link)
		print(str(j) + '题目：' + name + '  链接：' + link)

print('共找到唐诗 '+ str(len(weblinks)) + '首')

n = 0
for web in weblinks[0:20]:
	n += 1
	print(web)
	res2 = requests.get(web,headers=headers)
	soup2 = BeautifulSoup(res2.text,"lxml")
	shi = soup2.find_all('div',{'class':'cont'})[1]
	# print(shi.find('h1').get_text())
	timu = shi.find('h1').text
	names = shi.find_all('a')
	name = names[1].text + '（' + names[0].text + '）'
	shiwen = shi.find('div',class_='contson').text
	# print(timu + '\n' + name + '\n' + shiwen.replace(' ','').replace('\r','').replace('\n','') + '\n')
	with open('gushi.txt', 'a+') as f:
		f.write('第' + str(n) + '首：' + timu + '\n' + name + '\n' + shiwen.replace(' ','').replace('\r','').replace('\n','') + '\n' + '\n')
f.close()
print('爬取结束!，共打印了古诗 ' + str(n) + ' 首。')
