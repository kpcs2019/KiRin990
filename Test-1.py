# -*- coding:utf-8 -*-

# import turtle
# print("Hello，易语言，您是我的骄傲！")
# city = '广东省深圳市'
# name = '任正非'
# print('热烈祝贺来自中国{}的华为公司董事长：{}先生荣获杰出科技奖！'.format(city,name))

# turtle.penup()
# turtle.goto(20,40)
# turtle.pensize(5)
# turtle.color('red')
# turtle.pendown()
# i = 1
# while i < 6:
#     turtle.forward(200)
#     turtle.right(144)
#     i += 1
# turtle.done()

# import pkuseg

# myText = '群众观念淡化，宗旨意识不强。群众观念是我党建党发展、立党执政的重要法宝'
# seg = pkuseg.pkuseg()
# text = seg.cut(myText)
# print(text)

# import pymongo
# myclicent = pymongo.MongoClient('localhost',27017)
# mydata = myclicent['mydata']
# mycol = mydata['lagou']

# mylist = {
#     '公司全名':'中国深圳华为公司',
#     '公司简称':'中国华为',
#     '招聘职位':'高级软件架构师',
#     '月薪待遇':'20K-35K'
# }
# mycol.insert_one(mylist)

# keyword = input('请输入公司简称：')
# for col in mycol.find():
#     # print(list(col.values())[1:5])
#     compu = list(col.values())[2]
#     print(compu)
#     if keyword == compu:
#         print('{}本次招聘职位是：'.format(keyword) + list(col.values())[3])
#         break
#     else:
#         print('对不起，没有{}的招聘信息。'.format(keyword))
#         continue

# import re

# myword = "http://tool.oschina.net 1382868 中国，您好！kpjack@hotmail.com 0750-2291328 Demon"
# result = re.match('^http.*?(\d+).*?(\d+).*?(\d+).*?Demon$',myword)
# print(len(myword))
# print(result[3])

