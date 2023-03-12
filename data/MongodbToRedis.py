import redis
import json
from csv import reader
# 连接redis数据库
redis= redis.Redis(host='192.168.56.10', port=6379, db=0)
#打开csv文件
with open('../rating/total_rating_data.csv', encoding='utf-8') as csvfile:
    # 读取csv文件
    bandreader = reader(csvfile)
    # 遍历每列数据 sid uid score列
    for row in bandreader:

        key="uid:"+ row[1]    #row[1]       uid列   key 为 uid:row[1]
        value= row[0]+":"+ row[2]    # sid列:score列  value 为 sid:score
        redis.lpush(key,value)   #lpush添加到redis数据库
