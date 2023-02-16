import json

import pandas as pd
pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.width", None)
def csv_to_json():
 df1 = pd.read_csv('../data/fuzhou_data.csv')
 del df1['Unnamed: 0']
 # print(df1)
 s='序号,中文名,景点排名,攻略数量,评论数量,旅游率,景区介绍,评分,地址,开放时间,门票,价格'
 s=s.split(',')
 src=[]
 src.append(i for i in s)

 df2 = pd.DataFrame(df1,columns=src)
 # print(df2)
 df1.to_json("new_data.json",force_ascii=False,orient='table',index=False)
 with open('new_data.json','r',encoding='utf-8') as fp:
  json_data=json.load(fp)
 return json_data

def main():
 print(csv_to_json())
if __name__ == '__main__':
    main()