import pandas as pd
import numpy as np
import re
pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.width", None)
def main():
  data=pd.read_csv('xiamen_data.csv')
  en=re.compile(r'[a-zA-Z]')
  cn=re.compile(r'[\u4e00-\u9fa5]')
  data['属地']='厦门'
  for i in data.index:
      data.loc[i,'中文名']="".join(cn.findall(data.loc[i,'景点名称']))
      data.loc[i,'英文名']="".join(en.findall(data.loc[i,'景点名称']))

  data.to_csv('xiamen_data.csv')
if __name__ == '__main__':
    main()
