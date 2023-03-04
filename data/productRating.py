import random


import pandas as pd
import faker
import numpy as np
import time, hashlib
import uuid
pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.width", None)
def main():
 f=faker.Faker("zh-cn")
 scene=pd.read_csv("../Scene_data/total_data.csv")
 scene_id=scene['sid']
 rating=pd.read_csv("../rating/total_rating_data.csv")
 ratingdata=rating['uid']

 # uid=data['uid']

 list=[]
 for i in range(3283):

   dic = {}
   dic['sid']=scene_id[i]
   dic['uid']=ratingdata[i]
   dic['score']=round(random.uniform(3,5))
   list.append(dic)
 df=pd.DataFrame(list)
 df.to_csv("../rating/test_rating.csv",index=False)

if __name__ == '__main__':
    main()