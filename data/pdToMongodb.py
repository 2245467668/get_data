from importlib import reload

import pandas as pd
import re
import sys
import json
from pymongo import MongoClient
reload(sys)

class MongoBase:
    def __init__(self,collection):
        self.collection=collection
        self.OpenDB()
    def OpenDB(self):

        host='localhost'
        port='27017'
        db='recommender'
        uri = "mongodb://localhost:27017/test"
        self.con = MongoClient(uri, connect=False)
        self.db=self.con['SceneRecommend']  #定义数据库名
        self.collection=self.db[self.collection]
    def closeDB(self):
        self.con.close()


if __name__ == '__main__':
    mongo = MongoBase('Scene') #定义collection表名
    dicts =pd.read_csv('../Scene_data/total_price_data.csv')
    dicts.loc[ : , ~dicts.columns.str.contains("^Unnamed")]
    df = pd.DataFrame(dicts)
    mongo.collection.insert(json.loads(df.T.to_json()).values())
    mongo.closeDB()
    print(json.loads(df.T.to_json()).values())

