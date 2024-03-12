from sanic import Sanic
from sanic.response import json
from sqlalchemy import create_engine, Column, Integer, String, Double
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from api.util import Util

app = Sanic("stock")

# 创建SQLite数据库引擎
engine = create_engine('sqlite:///stockName.db', echo=True)

# 创建基类
Base = declarative_base()


class Returns(Base):
    __tablename__ = 'returns'
    id = Column(Integer, primary_key=True)
    code = Column(String, index=True)
    name = Column(String)
    year = Column(String)
    start = Column(Double)
    end = Column(Double)
    status = Column(Integer, default=0)


# 创建会话
Session = sessionmaker(bind=engine)
session = Session()


@app.post('/stock')
async def stock(request):
    start_date = request.form.get("startDate")
    end_data = request.form.get("endDate")
    name = request.form.get("name")
    if not name:
        name = "AAPL"
    nlist = Util.get_percent(start_date, end_data, name)
    return json({"list": nlist})


@app.get('/returns')
async def stock(request):
    code = request.form.get("code")
    if not code:
        code = "AAPL"
    list = session.query(Returns).filter_by(code=code)
    return json({"list": list})
# if __name__ == "__main__":
# app.run(host="0.0.0.0", port=8088)
