import pandas as pd
import re
import sys
import json
from pymongo import MongoClient



pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.width", None)
def main():
   beijing = pd.read_csv('../beijing_data.csv')
   shanghai = pd.read_csv('../shanghai_data.csv')
   chengdu = pd.read_csv('../chengdu_data.csv')
   hanzhou = pd.read_csv('../hangzhou_data.csv')
   xiamen = pd.read_csv('../xiamen_data.csv')
   nanjing = pd.read_csv('../nanjing_data.csv')

   # 合并数据
   new_data = pd.concat([beijing, shanghai, nanjing, hanzhou, xiamen, chengdu], ignore_index=True)
   # new_data['人气']=new_data['评论数量']+new_data['攻略数量']
   # 合并经纬度
   new_data['经纬度']=new_data[['经度','纬度']].apply(lambda x: pd.Series([x.values]),axis=1)
   #拆分景区英文名/中文名
   en = re.compile(r'[a-zA-Z]')
   cn = re.compile(r'[\u4e00-\u9fa5]')
   for i in new_data.index:
      new_data.loc[i, '中文名'] = "".join(cn.findall(new_data.loc[i, '景点名称']))
      new_data.loc[i, '英文名'] = "".join(en.findall(new_data.loc[i, '景点名称']))

   del new_data['英文名']
   del new_data['景点名称']
   new_data.rename(columns={'中文名':'景点名称',"Unnamed: 0":"sid"},inplace=True)

   data=new_data.pop("景点名称")
   new_data.insert(0,"景点名称",data)

   new_data.to_csv("../Scene_data/total_data.csv",index=False)




if __name__ == '__main__':
    main()
