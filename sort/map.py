
import numpy as np
import pandas as pd

pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.width", None)

def main():
    df = pd.read_csv('new_data.csv')
    # df[df['景点排名'].str.contains('%') == True] = np.nan
    # df[df['评分'].str.contains('--')==True]=np.nan
    # df.dropna(axis=0,subset=["景点排名"],inplace=True)
    # df.dropna(axis=0, subset=['地址'], inplace=True)

    df.sort_values(by=['攻略数量', '评论数量'], ascending=[False, False], inplace=True)
    # 索引重新排列
    data = df.head(5).reset_index(drop=True)
    print(data)
if __name__ == '__main__':
    main()