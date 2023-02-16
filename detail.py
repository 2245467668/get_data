import time
from bs4 import BeautifulSoup

import pandas as pd
import re
import numpy as np
import csv
import json
import requests
import random

pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.width", None)



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Referer': 'https://travel.qunar.com/',
    # 'Accept':'*/*',
    'Cookie': 'HMACCOUNT=5FC3320B42F5E4C4; BAIDUID=C00B3AEC25520094F38EC6A0FB9E0CC1:FG=1; ab_sr=1.0.1_NTA4OTVkMWNiMDI4MDM4ZmQxMjkwNmFmZmQyMzQ2ZWVhMzkxN2E0MDJkNzdmNTI4NThmNjUyMTZlMDhiMjc3MDJjYzU5MzA4YTE0Njc4YjdjNTExZTZiZDAwODNjNzBmZjQyNzNmYTE1ZDlmYWJmODMwZTZjYTE3ZjZiMTJiZDllOTBhNzIxYTY5MGQ2NDc3ZDU5NmQ0ZWVmNjM1MjY1Yg==',
    # 'Connection':'keep-alive',
    #  'Host':'hm.baidu.com',
    # 'Accept-Encoding':'gzip, deflate, br',
    # 'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Sec-Fetch-Dest':'script',
    #  'Sec-Fetch-Mode':'no-cors',
    #  'Sec-Fetch-Site':'cross-site'
}

cn_title = []
en_title = []
strategy = []
rank = []
comment = []
lvyou = []
intro = []
detail_url_list = []
data = {}
rating = []
address = []
open_time = []
ticket= []
price=[]



# 请求网站数据
def get_data(web_url,file_name,pageSize):
    for i in range(1, pageSize):
        page=i
        try:
            url = web_url + str(i)
            response = requests.get(url=url, headers=headers)
            time.sleep(0.5)
            result = response.content.decode()
            # 循环追加爬取的数据
            for j in range(0, 10):
                # 中文名(.*?)表示标签的内容
              try:
                detail_url_list.append(
                    re.findall('<a data-beacon="poi" href="(.*?)" target="_blank" class="imglink">', result, re.S)[j])
              except:
                  pass
        except:
            pass



        for i in range(0, 10):
            detail_result = requests.get(url=detail_url_list[i], headers=headers).text
            #html格式
            Obj = BeautifulSoup(detail_result,'lxml')
            time.sleep(2)
            # try:
            # for j in range(0,1):
            #     question=re.findall('<div class="MsgTitle">(.*?)</div>', detail_result, re.S)
            #     print(question)
            # if question==['尊敬的用户,您访问的页面可能不存在']:
            #        rating.insert(i + 1, None)
            #        address.insert(i + 1, None)
            #        open_time.insert(i + 1, None)
            #        price.insert(i + 1, None)
            #        question.clear()

            # <span class="cur_score">4.5</span>
            try:
             rating.append(Obj.find('span',{'class':'cur_score'}).text)
             print(rating)
             address.append(Obj.find('td',{'class':'td_l'}).find('span').text)
             print(address)
             open_time.append(Obj.find('dl',{'class':'m_desc_right_col'}).find('p').text)
             print(open_time)
             price.append(Obj.find('span',{'class':'e_price_txt'}).text)
             print(price)
             ticket.append(Obj.find('div',{'class':'e_db_content_box e_db_content_dont_indent'}).find('p').text)
             print(ticket)
            except:
                pass


        data = {
             '评分': rating,
            '地址': address,
            '开放时间': open_time,
            '门票':ticket,
            '价格':price
        }

        df = pd.DataFrame(pd.DataFrame.from_dict(data, orient='index').values.T, columns=list(data.keys()))

        print(df)

        write_data(df,page,file_name)
    # 获取详情页的信息


# 写入数据
def write_data(df,page,file_name):
    df.to_csv(file_name)
    print("写入成功"+'第'+str(page)+'页爬完')


def main():
    url = "https://travel.qunar.com/p-cs299821-longyan-jingdian-1-"
    file_name = "longyan_data.csv"
    pageSize = 3
    get_data(url,file_name,pageSize)


if __name__ == '__main__':
    main()
