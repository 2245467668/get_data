import re
import time
from itertools  import islice
import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_url(n):
    lst = []
    for i in range(n):
        ui = "https://travel.qunar.com/p-cs300195-hangzhou-jingdian-1-{}".format(i + 1)
        lst.append(ui)
    return lst


def get_detail_raing(url, dic_heders, dic_cookies):
    time.sleep(1)
    ri = requests.get(url, headers=dic_heders, cookies=dic_cookies)
    result = ri.content.decode()

    soup = BeautifulSoup(ri.text, 'lxml')
    # print(soup.find(id="js_replace_box").text)

    ul = soup.find(id="comment_box")  # 获取评论区标签 //问题
    CommentList = ul.find_all('li')  # 评论列表 由li组成

    list = []
               # islice(list,10)  切片选取前10个数据
    for item in CommentList[:100]:  #切片限制10条评论
        dic = {}
        time.sleep(1)
        # item 表示一条评论 li

        for x in item.find_all('div', class_="e_comment_usr_name"):
            time.sleep(1.5)
            items = x.select('a')[0]  # uid
            uid = re.findall(r"\d+\.?\d*", items.get('href'))[0]  # uid
            dic['sid'] = re.findall(r"\d+\.?\d*", url)[0]
            dic['uid'] = uid

        # print(re.findall(r"\d+\.?\d*", soup.find_all('div', class_="e_comment_usr_name")[0].select('a')[0].get('href'))[0])
        for y in item.find_all('span',class_="total_star"): #找到 class=total_star 的span标签
            time.sleep(1.5)
            span=y.select('span')[0]      #找到下一个span标签
            starRating = re.findall(r"\d+\.?\d*", str(span))[0]  #筛选出评分数字
            dic['score'] = int(starRating)

            list.append(dic)
            print(dic)

    print(list)
    return list


def get_data(ui, dic_heders, dic_cookies):
    global lis
    time.sleep(1)
    ri = requests.get(ui, headers=dic_heders, cookies=dic_cookies)

    soup_i = BeautifulSoup(ri.text, 'lxml')
    try:
     ul = soup_i.find("ul", class_="list_item clrfix")
     lis = ul.find_all('li')  # lis列表
    except:
        print("错误")
        pass

    lst = []
    DetailUrl = []  # 详情页连接
    for li in lis:

        DetailUrl.append(li.find('a', class_="imglink")['href'])

    # print(lst)

    return DetailUrl


if __name__ == "__main__":

    dic_heders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    dic_cookies = {}
    cookies = 'QN1=0000630034fc494158f84e2b; QN269=6E5FA2C163C211ED932DFA163EC565DF; _i=RBTjeLTng0_ILMEwUcFfwgTlJ-xx; fid=a155d058-65f9-4914-a88c-0a240ff8439b; QN48=tc_872d3f66b774d6db_18473ed3d8c_1d63; QN300=common.qunarzz.com; QN57=16684757760020.03164921539707377; QN58=1668665897758%7C1668665926996%7C3; QN99=7092; QunarGlobal=10.68.64.14_-6f12bbb6_18492826a58_-44dd|1668907165141; QN601=96174c9b436f1910007b00b33f386f88; QN205=organic; QN277=organic; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; csrfToken=LUejInc8Fw8io6YoViDyLBkmpLS3cfmz; Hm_lvt_c56a2b5278263aa647778d304009eafc=1669530020,1669634326,1669786172,1669794077; viewpoi=6200527|35036897|14873349|3231402|710971|715901|3234233|710603|10075789|706064|10022236|9164289|9506504|7564962|27339285|9151246; _vi=PKaGLINIMT4DgHdroamkCC4l8J27rLUlLY8jcdN2L7CkTmlgXx2QSlH-31z4-05Do3bV4MOrTBzIBclbKruOoJFTY3kUncU3hS21C93Bd_sBhhB3OShq_6BXtZ2HvueKxi81HCaGFfCldnA4WC1SXlvr7V-_-naf82qsV-xBmsL8; JSESSIONID=EB6CA31CF3AFED351E3760CE89239F83; viewdist=300026-1|299782-228|299826-58|299779-7|299781-8|299821-9|300015-4|296876-2|299914-4|300011-1|299784-2|299878-2; uld=1-299782-417-1669795270|1-299826-70-1669794822|1-297214-1-1669794286|1-297217-5-1669794265|1-299878-2-1669794143|1-299914-5-1669794133|1-299784-2-1669794118|1-300011-1-1669794110|1-300015-4-1669794091|1-299779-8-1669430579|1-297170-3-1669365573|1-297215-1-1668906765|1-299781-10-1668856120|1-300195-2-1668776746|1-297222-7-1668776602|1-299821-16-1668776004; ariaDefaultTheme=undefined; Hm_lpvt_c56a2b5278263aa647778d304009eafc=1669795272; SECKEY_ABVK=3ykrC2kmpxQfyp9xVrq5JXaFPZarTESb9FjXrSbY/JE%3D; QN271=4db8e230-7f93-45a8-96bf-cfd347a17eb1; BMAP_SECKEY=e8LjJa3JdI9oyMPDsMcOcyWunjzd9xgUQ_UKV6SDPL0nqFzZ_bcmYhOQGp3gArqegyRCFPrIP-SmLF3gfV5PfZGKjdl1h8_fX_Y64gaPY8gjTSlMvZ2pkNd4qVYfRGpswl3hJ6DojT0aRxtIu5LnxTxO-wNrHZJi4hDUcRRbN5jGBsvH7fUhhCkAm5gnu5su; QN267=2005490675ae14f3d6'
    cookies_lst = cookies.split(";")
    for i in cookies_lst:
        dic_cookies[i.split("=")[0]] = i.split("=")[1]

    dataset = []
    for u in get_url(7):
        for url in get_data(u, dic_heders, dic_cookies):  # 遍历url列
            try:
                dataset.extend(get_detail_raing(url, dic_heders, dic_cookies))  # 获取详情页评分数据
                print('数据采集成功，共采集数据{}条'.format(len(url)))

            except:
                continue
                print('数据采集失败，网址为：', url)

            df = pd.DataFrame(dataset)
            df.to_csv('rating/hangzhou_rating.csv', index=False)
            print("写入成功")
