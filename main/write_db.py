import pandas as pd
from sqlalchemy import create_engine

def main():
    df=pd.read_csv("../data/new_data.csv")
    connect = create_engine("mysql+pymysql://root:123456@localhost:3306/python_bigdata?charset=utf8")
    df.to_sql(name="scene", con=connect, if_exists='replace', index=True)
if __name__ == '__main__':
    main()