import requests
import json
import time
import pymongo

class LaGou():
    def __init__(self):
        self.temp_url = 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput='
        self.base_url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
        self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
                       (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
                       'Referer': 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput=',
                       'Host': 'www.lagou.com'}

        self.client = pymongo.MongoClient('localhost', 27017) # 链接数据库
        self.mydb = self.client['mydata']
        self.lagou = self.mydb['lagou']
        self.page_count = 0

    def get_page(self, url, params, session):
        try:
            session.get(url = lagou.temp_url, headers = lagou.header, timeout = 10)
            cookie = session.cookies # 获取cookie
            html = requests.post(self.base_url, data=params, headers=self.header, cookies=cookie)
            json_data = json.loads(html.text)
            results = json_data['content']['positionResult']['result']
            result_count = json_data['content']['positionResult']['totalCount'] # 所有数据的个数
            self.page_count = int(result_count) // 15 

            for result in results:
                infos = {
                    '公司全名':result['companyFullName'],
                    '公司简称':result['companyShortName'],
                    '招聘职位':result['positionName'],
                    '月薪待遇':result['salary']
                }
                self.lagou.insert_one(infos)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    params = {
        'first': 'true',
        'pn': '1',
        'kd': '爬虫'
        }
    lagou = LaGou()
    s = requests.session() # 建立session
    lagou.get_page(lagou.base_url,params, s)
    # for i in range(2, lagou.page_count):
    #     params = {
    #     'first': 'true',
    #     'pn': str(i),
    #     'kd': '爬虫'
    #     }
    #     lagou.get_page(lagou.base_url,params, s)
    #     time.sleep(3)

