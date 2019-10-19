from urllib import request
import requests,re,os,threading
from bs4 import BeautifulSoup

image_regex = r'<img alt=".*" src="(.*?)">*'
url = 'http://www.meizitu.com/a/5491.html'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3026.3 Safari/537.36'}

req = request.Request(url=url,headers=header)
page_info = request.urlopen(req).read().decode('gbk')

path = 1
page_urls = []
thread = []

soup = BeautifulSoup(page_info,'html.parser')
a_list = soup.find_all('li')


for info in a_list:
    try:
        url = info.a['href']
    except Exception as e:
        pass
    else:
        if url.startswith('http://www.meizitu.com/a/'):
            page_urls.append(url)
else:
    page_urls = list(set(page_urls))

def pageinfo(url):
    req = request.Request(url=url, headers=header)
    page_info = request.urlopen(req).read().decode('gbk')
    return page_info


def download(url,path):
    page_info =  pageinfo(url)
    image_urls = re.findall(image_regex,page_info)
    save  = 'd:/meizitu/%d'
    1 if os.path.exists(save%path) else os.makedirs(save%path,mode=777)
    for url in image_urls:
        data = requests.get(url,stream=True,headers=header)
        filename = url.rsplit('/',1)[-1]
        with open(save%path+'/'+filename,'ab+') as f:
            f.write(data.content)
        print('%s download done...'%filename)

for url in page_urls:
    t = threading.Thread(target=download,args=(url,path))
    t.start()
    thread.append(t)
    path += 1

for th in thread:
    th.join()
