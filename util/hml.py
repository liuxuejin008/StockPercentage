import re
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建SQLite数据库引擎
engine = create_engine('sqlite:///stockName.db', echo=True)

# 创建基类
Base = declarative_base()

# 定义数据模型
class Code(Base):
    __tablename__ = 'code'
    id = Column(Integer, primary_key=True)
    code = Column(String)
    name = Column(String)

# 创建数据表
Base.metadata.create_all(engine)

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()


# 读取HTML文件内容
with open('/Users/liuxujein/Downloads/dist/stockname.html', 'r', encoding='utf-8') as file:
    html_content = file.read()


# 提取目标内容
pattern = r'<a class="us-stock-company" target="_blank" href="/analysis/(\w+)">\s+\(<span class="us-stock-company-ticker">(\w+)</span>\)\s*(.*?)\s*</a>'
match = re.findall(pattern, html_content)
print(len(match))

try:
    if match:
        for item in match:
            # 添加数据
            code = item[1].strip()
            name = item[2].strip()
            new_code = Code(code=code, name=name)
            print(new_code)
            session.add(new_code)
            # 提交事务
            session.commit()

    else:
        print("No match found.")

    print("=====================================")
    users = session.query(Code).all()
    for user in users:
        print(f'ID: {user.id}, Name: {user.name}, Age: {user.code}')
    # 关闭会话
    session.close()

except Exception as e:
    # 发生异常时执行回滚操作
    print(f"An error occurred: {e}")
