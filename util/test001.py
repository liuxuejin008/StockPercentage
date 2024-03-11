from sqlalchemy import create_engine, Column, Integer, String, Double
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
import yfinance as yf
from api.util import Util
from util.hml import Code

# 创建SQLite数据库引擎
engine = create_engine('sqlite:///stock.db', echo=True)

# 创建基类
Base = declarative_base()


# 定义数据模型
class Returns(Base):
    __tablename__ = 'returns'
    id = Column(Integer, primary_key=True)
    code = Column(String,index=True)
    name = Column(String)
    year = Column(String)
    start = Column(Double)
    end = Column(Double)
    status = Column(Integer,default=0)





#创建会话
Session = sessionmaker(bind=engine)
session = Session()


users = session.query(Code).all()
for user in users:
    print(f'ID: {user.id}, Name: {user.name}, Age: {user.code}')
    # 关闭会话
    # 计算每一年的收益
    for i in range(0, 6):
        try:
            year = 2018 + i
            start_date = str(year) + "-01-01"
            end_date = str(year) + "-01-10"
            returns = Returns()
            returns.year = str(year)
            stock = yf.Ticker(user.code)
            returns.code = user.code
            returns.name = user.name
            history = stock.history(start=start_date, end=end_date)
            df = pd.DataFrame(history, columns=['Open', 'High', 'Low', 'Close'])
            start_open = 0
            start_High = 0
            start_Close = 0
            start_Low = 0
            first_row = df.head(1)
            print(first_row['Close'].values[0])
            start = first_row['Close'].values[0]
            returns.start = start
            start_date = str(year) + "-12-20"
            end_date = str(year) + "-12-31"
            history = stock.history(start=start_date, end=end_date)
            df = pd.DataFrame(history, columns=['Open', 'High', 'Low', 'Close'])
            start_open = 0
            start_High = 0
            start_Close = 0
            start_Low = 0
            last_row = df.tail(1)
            print("---------------------------")
            print(df)
            print(last_row['Close'].values[0])
            end = last_row['Close'].values[0]

            print("---------------------------")
            returns.end = end

            session.add(returns)
            # 提交事务
            session.commit()

        except Exception as e:
            #发生异常时执行回滚操作
            print(f"An error occurred: {e}")





