from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 配置数据库连接
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/t_ai')
Session = sessionmaker(bind=engine)
Base = declarative_base()


# 定义用户模型
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))


# 创建表
Base.metadata.create_all(engine)
