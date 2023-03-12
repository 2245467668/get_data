import jieba
import jieba.analyse
import pandas as pd
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
text = '京郊少见的北方水镇，建筑古韵十足，泡温泉、登长城'

# 提取关键词，设置数量为 3

data=pd.read_csv("../Scene_data/total_price_data.csv")
data.dropna(axis=0, how='any',inplace=True)
values=[]
i = 0
for item in  data['introduce']:

    keywords = jieba.analyse.extract_tags(item, topK=3)

    try:
     value=keywords[0]+"|"+keywords[1]+"|"+keywords[2]
     i = i + 1
     values.append(value)
    except:
       values.append(value)
       continue



data['tag']=values
data.to_csv('tag.csv',columns={'sid','tag'}, index=False)

rating=pd.read_csv("../rating/total_rating_data.csv")
tag=pd.read_csv("tag.csv")
mergedata=tag.merge(rating,how='inner',on='sid')   #合并两个文件
mergedata.to_csv("tag_rating.csv",index=False)

print(data)



# print(keywords)