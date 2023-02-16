import time
import pandas as pd
import re
import numpy as np
import csv
import json
import requests
from bs4 import BeautifulSoup
import random

pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.width", None)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    # 'Accept':'*/*',
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
ticket = []
price = []
cost = []


# 请求网站数据
def get_data(web_url, file_name, pageSize):
    for i in range(1, pageSize):
        page = i
        if i == 6 or i == 23 or i == 76 or i == 115:
            pass
        else:
            url = web_url + str(i)
            print(url)
            response = requests.get(url=url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            time.sleep(2)

            # 循环追加爬取的数据
            for j in range(0, 10):

                # 中文名(.*?)表示标签的内容
                try:
                    # 名称
                    cn_title.insert(j + (page - 1) * 10, soup.find_all(class_="cn_tit")[j].text)
                except:
                    cn_title.insert(j + (page - 1) * 10, None)
                    pass
                try:
                    cost.insert(j + (page - 1) * 10, soup.find_all(class_="sub_des", text=re.compile('¥ '))[j].text)
                except:
                    cost.insert(j + (page - 1) * 10, None)
                    pass
                try:
                    rating.insert(j + (page - 1) * 10, soup.find_all(class_="cur_score")[j].text)
                except:
                    rating.insert(j + (page - 1) * 10, None)
                    pass
                try:
                    comment.insert(j + (page - 1) * 10, soup.find_all("span",class_="txt")[j].text)
                except:
                    comment.insert(j + (page - 1) * 10, None)
                    pass

                #    cn_title.append(re.findall('class="cn_tit">(.*?)</span></a>',result, re.S)[j])
                #
                #    cost.append(re.findall('<dd class="sub_des">(.*?)</dd>', result, re.S)[j])
                #    #评分
                #    rating.append(re.findall('class="scorebox"><span class="cur_score">(.*?)</span>',result,re.S)[j])
                #    # 评论
                #    # comment.append(re.findall('class="txt">(.*?)<span class="img_doublequote img_r"></span></span>',result,re.S)[j])
                # except:
                #     pass

        print("第几页", i)

        data = {
            '中文名': cn_title,
            '消费': cost,
            '评分': rating,
            '评论': comment,

        }

        df = pd.DataFrame(pd.DataFrame.from_dict(data, orient='index').values.T, columns=list(data.keys()))
        print(df)

        write_data(df, page, file_name)
    # 获取详情页的信息


# 写入数据
def write_data(df, page, file_name):
    df.to_csv(file_name)
    print("写入成功" + '第' + str(page) + '页爬完')


def main():
    get_data()


if __name__ == '__main__':
    main()
