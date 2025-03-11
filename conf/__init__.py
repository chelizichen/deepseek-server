# 导入必要的模块和类
from conf.conf import SgridConfig
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 定义初始化配置的函数
def init_config():
    # 创建 SgridConfig 实例
    config = SgridConfig()
    # 初始化配置
    config.init_config()
    return config

# 初始化配置
sgrid_config = init_config()

# 获取数据库连接配置
db_config = sgrid_config.get("config.db")

# 检查数据库配置是否存在
if db_config:
    # 配置数据库连接
    engine = create_engine(db_config, pool_pre_ping=True, isolation_level="REPEATABLE READ")
    # 创建会话工厂
    Session = sessionmaker(bind=engine)
    # 创建基类
    Base = declarative_base()
else:
    # 若数据库配置不存在，抛出异常
    raise ValueError("Database configuration 'config.db' not found.")