import time
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
        if i == 6 or i == 23 or i == 76 or i == 115:
            pass
        else:
            url = web_url + str(i)
            print(url)
            response = requests.get(url=url, headers=headers)
            time.sleep(0.5)
            result = response.content.decode()
            # 循环追加爬取的数据
            for j in range(0, 10):
                # 中文名(.*?)表示标签的内容
             try:
                cn_title.append(re.findall('class="cn_tit">(.*?)<span class="en_tit">', result, re.S)[j])
                # 英文名
                # en_title.append(re.findall('<span class="en_tit">(.*?)</span>', result, re.S)[j])
                # 排名
                rank.append(
                    re.findall('<span class="ranking_sum">.*?<span class="sum">(.*?)</span>', result, re.S)[j])
                # 攻略数量
                strategy.append(re.findall('class="icon_strategy" title="攻略"></span>(.*?)</div>', result, re.S)[j])
                # 评论数量
                comment.append(
                    re.findall('<div class="comment_sum"><span class="icon_comment" title="点评"></span>(.*?)</div>'
                               , result, re.S)[j])
                # 有多少驴友去过
                lvyou.append(
                    re.findall('<span class="comment_sum"><span class="sum">(.*?)</span>.*?</span>', result, re.S)[j])
                intro.append(re.findall('<div class="desbox">(.*?)</div>', result, re.S)[j])
                detail_url_list.insert(j,re.findall('<a data-beacon="poi" href="(.*?)" target="_blank" class="imglink">', result, re.S)[j])
             except:
                 pass



        print("第几页",i)
        detail_size= len(detail_url_list)
        print('有几个url',detail_size)
        for i in range(0, detail_size):
            detail_result = requests.get(url=detail_url_list[i], headers=headers).content.decode()
            time.sleep(3)
            # try:
            print(i+(page-1)*10)
            try:
                rating.insert(i+(page-1)*10,re.findall('<span class="cur_score">(.*?)</span>', detail_result, re.S)[0])
            except:
                rating.insert(i+(page-1)*10,None)
            try:
                address.insert(i+(page-1)*10,re.findall('<dd><span>(.*?)</span></dd>', detail_result, re.S)[0])
            except:
                address.insert(i+(page-1)*10,None)
            try:
                open_time.insert(i+(page-1)*10,re.findall('<dd><span><p>(.*?)</p></span></dd>', detail_result, re.S)[0])
            except:
                open_time.insert(i+(page-1)*10,None)
            try:
                price.insert(i+(page-1)*10,re.findall('<span class="e_price_txt"><i class="rmb">.*?</i>(.*?)</span>',
                                                  detail_result, re.S)[0])
            except:
                price.insert(i+(page-1)*10,None)
                pass
            try:
               ticket.insert(i+(page-1)*10,re.findall('<div class="e_db_content_box e_db_content_dont_indent"><p>(.*?)</p></div>', detail_result, re.S)[0])
            except:
                ticket.insert(i+(page-1)*10,None)
                pass
        detail_url_list.clear()

        data = {
            '中文名': cn_title,
            # '英文名': en_title,
            '景点排名': rank,
            '攻略数量': strategy,
            '评论数量': comment,
            '旅游率': lvyou,
            '景区介绍': intro,
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
    get_data()


if __name__ == '__main__':
    main()
