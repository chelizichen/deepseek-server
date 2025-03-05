from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, TEXT, DATETIME
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from conf import sgrid_config

# 配置数据库连接
print("config.db: ", sgrid_config.get("config.db"))
engine = create_engine(sgrid_config.get("config.db"),isolation_level="READ COMMITTED")
Session = sessionmaker(bind=engine)
Base = declarative_base()


# 定义用户模型
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    phone = Column(String(255))
    create_time = Column(DATETIME)


class Chats(Base):
    __tablename__ = 'chats'
    """
    用户对话记录表
    每次对话后，将对话记录到库中
    系统定时对已有的对话内容进行分析和摘要
    保持对话的长度和精度
    """

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    question = Column(TEXT)
    answer = Column(TEXT)
    """
    type 为 记录类型
    1. 为普通类型，即 用户正常提问
    2. 为摘要类型，即 系统对用户的提问进行了摘要说明
    摘要类型插入时默认为 2
    """
    type = Column(Integer)
    """
    answer_type 为 回答类型
    1. 为普通类型
    2. 为用户推荐类型
    3. 为用户丢弃类型
    """
    answer_type = Column(Integer)
    create_time = Column(DATETIME)
    session_id = Column(Integer)


class Sessions(Base):
    __tablename__ = 'sessions'
    """
    会话记录表
    """
    id = Column(Integer, primary_key=True)
    create_user_id = Column(Integer)
    name = Column(String(255))
    create_time = Column(DATETIME)


class Prompts(Base):
    __tablename__ = 'prompts'
    """
    提示词表
    """
    id = Column(Integer, primary_key=True)
    name = Column(TEXT)  # 提示词名称
    use_count = Column(Integer)  # 使用次数
    create_user_id = Column(Integer)  # 创建用户id
    create_time = Column(DATETIME)

# 会话提示词表
class ChatsPrompts(Base):
    __tablename__ = 'chats_prompts'
    """
    聊天记录和提示词关联表
    """
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer)
    user_id = Column(Integer)
    prompt_id = Column(Integer)


# 创建表
Base.metadata.create_all(engine)
