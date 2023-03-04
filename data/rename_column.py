import pandas as pd
import re
import sys
import json
from pymongo import MongoClient



pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.width", None)
def main():
   data = pd.read_csv('../Scene_data/total_data.csv')

   data.rename(columns={"景点名称":"Scene_name","攻略数量":"strategy_num","评分":"rating","景区介绍":"introduce","景点排名":"rank",
                        "经度":"longitude","纬度":"latitude","旅游率":"tourist_ratio","评论数量":"rating_num","图片url":"img_url","经纬度":"longAndlat"},inplace=True)

   # data.dropna(inplace=True)
   data.to_csv("../Scene_data/total_data.csv",index=False)




if __name__ == '__main__':
    main()
