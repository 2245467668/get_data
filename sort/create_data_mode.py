import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.width", None)

# 汉字字体，优先使用楷体，找不到则使用黑体
plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']
# 正常显示负号
plt.rcParams['axes.unicode_minus'] = False

def clean_data():
    df = pd.read_csv('new_data.csv')
    del df['Unnamed: 0'] ,df['旅游率'],df['景区介绍'],df['地址'], df['开放时间'],df['门票']
    df[df['景点排名'].str.contains('%') == True] = np.nan
    df[df['评分'].str.contains('--') == True] = np.nan
    df[df['攻略数量'] == 0] = np.nan
    df[df['评分'] ==0] = np.nan
    df.dropna(axis=0,subset=['价格'],inplace=True)
    df.dropna(axis=0, subset=["景点排名"], inplace=True)
    df.dropna(axis=0,subset=['评分'],inplace=True)
    df.dropna(axis=0, subset=['攻略数量'], inplace=True)
    print(df)
    # df['景点排名'] = df['景点排名'].astype(int)
    # df['评分'] = df['评分'].astype(float)
    # sns.heatmap(df[['价格','景点排名','评分','攻略数量']].corr())
    # plt.show()
    df.to_csv('data_heatmap.csv')
def main():
    clean_data()


if __name__ == '__main__':
    main()
