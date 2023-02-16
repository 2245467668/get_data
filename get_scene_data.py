import re
import time

import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_url(n):
    lst = []
    for i in range(n):
        ui = "https://travel.qunar.com/p-cs299861-nanjing-jingdian-1-{}".format(i + 1)
        lst.append(ui)
    return lst


def get_data(ui, d_h, d_c):
    global dic, dls
    ri = requests.get(ui, headers=dic_heders, cookies=dic_cookies)
    time.sleep(1)
    soup_i = BeautifulSoup(ri.text, 'lxml')
    ul = soup_i.find("ul", class_="list_item clrfix")
    lis = ul.find_all('li')  # lis列表
    detailUrl = []
    lst = []

    for li in lis:
        time.sleep(2)
        dic = {}
        dic['sid'] = re.findall(r"\d+\.?\d*", li.find('a', class_="imglink")['href'])[0]  # sid 从url中提取数字作为id
        print(re.findall(r"\d+\.?\d*", li.find('a', class_="imglink")['href'])[0])
        dic['景点名称'] = li.find('span', class_="cn_tit").text
        dic['攻略数量'] = li.find('div', class_="strategy_sum").text
        dic['评分'] = li.find('span', class_="total_star").span['style']
        dic['景区介绍'] = li.find('div', class_="desbox").text
        dic['景点排名'] = li.find('span', class_="ranking_sum").text
        dic['经度'] = li['data-lng']
        dic['纬度'] = li['data-lat']
        dic['评论数量'] = li.find('div', class_="comment_sum").text
        dic['旅游率'] = li.find('span', class_="comment_sum").span.text
        dic['图片url'] = li.find('a', class_="imglink").img['src']
        url = requests.get(li.find('a', class_="imglink")['href'], headers=dic_heders, cookies=dic_cookies)

        soup = BeautifulSoup(url.text, 'lxml')
        div = soup.find("div", class_="e_ticket_info")
        dls = div.find_all('dl')
        for dl in dls:
            # price=.text
            # print(price)
         dic['价格'] = dl.find('dd', class_="e_now_price").span.text
        lst.append(dic)
    print(lst)

    return lst
    # 获取价格


if __name__ == "__main__":

    dic_heders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    dic_cookies = {}
    cookies = 'QN1=0000630034fc494158f84e2b; QN269=6E5FA2C163C211ED932DFA163EC565DF; _i=RBTjeLTng0_ILMEwUcFfwgTlJ-xx; fid=a155d058-65f9-4914-a88c-0a240ff8439b; QN48=tc_872d3f66b774d6db_18473ed3d8c_1d63; QN300=common.qunarzz.com; QN57=16684757760020.03164921539707377; QN58=1668665897758%7C1668665926996%7C3; QN99=7092; QunarGlobal=10.68.64.14_-6f12bbb6_18492826a58_-44dd|1668907165141; QN601=96174c9b436f1910007b00b33f386f88; QN205=organic; QN277=organic; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; csrfToken=LUejInc8Fw8io6YoViDyLBkmpLS3cfmz; Hm_lvt_c56a2b5278263aa647778d304009eafc=1669530020,1669634326,1669786172,1669794077; viewpoi=6200527|35036897|14873349|3231402|710971|715901|3234233|710603|10075789|706064|10022236|9164289|9506504|7564962|27339285|9151246; _vi=PKaGLINIMT4DgHdroamkCC4l8J27rLUlLY8jcdN2L7CkTmlgXx2QSlH-31z4-05Do3bV4MOrTBzIBclbKruOoJFTY3kUncU3hS21C93Bd_sBhhB3OShq_6BXtZ2HvueKxi81HCaGFfCldnA4WC1SXlvr7V-_-naf82qsV-xBmsL8; JSESSIONID=EB6CA31CF3AFED351E3760CE89239F83; viewdist=300026-1|299782-228|299826-58|299779-7|299781-8|299821-9|300015-4|296876-2|299914-4|300011-1|299784-2|299878-2; uld=1-299782-417-1669795270|1-299826-70-1669794822|1-297214-1-1669794286|1-297217-5-1669794265|1-299878-2-1669794143|1-299914-5-1669794133|1-299784-2-1669794118|1-300011-1-1669794110|1-300015-4-1669794091|1-299779-8-1669430579|1-297170-3-1669365573|1-297215-1-1668906765|1-299781-10-1668856120|1-300195-2-1668776746|1-297222-7-1668776602|1-299821-16-1668776004; ariaDefaultTheme=undefined; Hm_lpvt_c56a2b5278263aa647778d304009eafc=1669795272; SECKEY_ABVK=3ykrC2kmpxQfyp9xVrq5JXaFPZarTESb9FjXrSbY/JE%3D; QN271=4db8e230-7f93-45a8-96bf-cfd347a17eb1; BMAP_SECKEY=e8LjJa3JdI9oyMPDsMcOcyWunjzd9xgUQ_UKV6SDPL0nqFzZ_bcmYhOQGp3gArqegyRCFPrIP-SmLF3gfV5PfZGKjdl1h8_fX_Y64gaPY8gjTSlMvZ2pkNd4qVYfRGpswl3hJ6DojT0aRxtIu5LnxTxO-wNrHZJi4hDUcRRbN5jGBsvH7fUhhCkAm5gnu5su; QN267=2005490675ae14f3d6'
    cookies_lst = cookies.split("; ")
    for i in cookies_lst:
        dic_cookies[i.split("=")[0]] = i.split("=")[1]

    datalst = []
    errorlst = []
    for u in get_url(1):
        try:
            datalst.extend(get_data(u, dic_heders, dic_cookies))

            print('数据采集成功，共采集数据{}条'.format(len(datalst)))
        except:
            errorlst.append(u)
            print('数据采集失败，网址为：', u)

        df = pd.DataFrame(datalst)

        df['经度'] = df['经度'].astype('float')
        df['纬度'] = df['纬度'].astype('float')
        df['评论数量'] = df['评论数量'].astype('int')
        df['攻略数量'] = df['攻略数量'].astype('int')
        df['评分'] = df['评分'].str.split(":").str[-1].str.replace("%", "").astype("float")
        df['旅游率'] = df['旅游率'].str.replace("%", "").astype('float') / 100
        df['景点排名'] = df[df['景点排名'] != ""]['景点排名'].str.split("第").str[-1].astype('int')

        df.to_csv('nanjing_data.csv', index=False)
