from sqlalchemy import create_engine, Column, Integer, String, Double
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建SQLite数据库引擎
engine = create_engine('postgresql://liuxuejin008:ElkMUaiweY71@ep-odd-moon-a57s014c-pooler.us-east-2.aws.neon.tech/stock?sslmode=require', echo=True)

# 创建基类
Base = declarative_base()

engine1 = create_engine('sqlite:///stockName.db', echo=True)

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()


# 创建会话
Session1 = sessionmaker(bind=engine1)
session1 = Session1()

class Returns(Base):
    __tablename__ = 'returns'
    id = Column(Integer, primary_key=True)
    code = Column(String, index=True)
    name = Column(String)
    year = Column(String)
    start = Column(Double)
    end = Column(Double)
    status = Column(Integer, default=0)

# 创建数据表
Base.metadata.create_all(engine)

# 查询数据
items = session1.query(Returns).all()
for item in items:
    print("================")
    print(f'ID: {item.id}, Name: {item.name}, Age: {item.code}')
    returns = Returns()
    returns.code = item.code
    returns.name = item.name
    returns.start = item.start
    returns.end  = item.end
    returns.year = item.year
    session.add(returns)
    session.commit()
# 关闭会话
session.close()