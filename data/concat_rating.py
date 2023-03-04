import pandas as pd
import re
import sys
import json
from pymongo import MongoClient


pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.width", None)
def main():
   beijing = pd.read_csv('../rating/beijing_rating.csv')
   shanghai = pd.read_csv('../rating/shanghai_rating.csv')
   chengdu = pd.read_csv('../rating/chengdu_rating.csv')
   hanzhou = pd.read_csv('../rating/hangzhou_rating.csv')
   xiamen = pd.read_csv('../rating/xiamen_rating.csv')
   nanjing = pd.read_csv('../rating/nanjing_rating.csv')

   # 合并数据
   new_data = pd.concat([beijing, shanghai, nanjing, hanzhou, xiamen, chengdu], ignore_index=True)


   new_data.to_csv("../rating/total_rating_data.csv",index=False)




if __name__ == '__main__':
    main()
