import json

import numpy as np
import pandas as pd

pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.width", None)


def concat_data():
        fuzhou_data = pd.read_csv('../data/xiamen_data.csv')
        xiamen_data = pd.read_csv('../data/fuzhou_data.csv')
        del xiamen_data['Unnamed: 0']
        del fuzhou_data['Unnamed: 0']

        new_data = pd.concat([fuzhou_data, xiamen_data], ignore_index=True)
        new_data.to_csv('new_data.csv')


def main():
        #合并数据

        df = pd.read_csv('new_data.csv')
        del df['Unnamed: 0']
        df[df['景点排名'].str.contains('%') == True] = np.nan
        df[df['评分'].str.contains('--')==True]=np.nan
        df.dropna(axis=0,subset=["景点排名"],inplace=True)
        df['景点排名']=df['景点排名'].astype(int)
        df['攻略数量']=df['攻略数量'].astype(int)
        df['评论数量'] = df['评论数量'].astype(int)
        df['评分'] = df['评分'].astype(float)

        xiamen_num=len(df[df['地址'].str.contains('厦门')==True])
        zhangzhou_num = len(df[df['地址'].str.contains('漳州')==True])
        quanzhou_num = len(df[df['地址'].str.contains('泉州')==True])
        fujzhou_num = len(df[df['地址'].str.contains('福州') == True])
        longyan_num=len(df[df['地址'].str.contains('龙岩') == True])
        print(longyan_num)
        # df.sort_values(by=['攻略数量','评论数量'],ascending=[False,False],inplace=True)
        #索引重新排列
        # data=df.head(5).reset_index(drop=True)
        # print(round(data['评论数量']/data['评论数量'].sum(),2))
        # print(round(data['攻略数量']/data['攻略数量'].sum(),2))
        # data['评论数量占比'] = round(data['评论数量'] / data['评论数量'].sum(), 2)
        # data['攻略数量占比']=round(data['攻略数量']/data['攻略数量'].sum(),2)
        # data['总占比']=data['评论数量占比']+data['攻略数量占比']
        # data['总占比']=data['总占比'].apply(lambda x: format(x,'.2%'))
        # print( data['总占比'])
        df.to_csv('scene_rank.csv')



if __name__ == '__main__':
    main()
