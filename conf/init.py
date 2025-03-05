import os

from yaml import load, FullLoader, parse
from pathlib import Path


class SgridConfig:
    def __init__(self, config_file="sgrid.yml"):
        self.config = None
        self.config_file = config_file

    def init_config(self):
        # yaml_text = """
        # server:
        #   name: DeepSeekServer
        #   host: 127.0.0.1
        #   port: 14232
        #   protocol: http
        #   language: python
        #   version: 3.10.12
        # config:
        #   api_key: sk-f0e1e656ba294b98a7ed892781df1ce9
        #   db: mysql+pymysql://root:lzy20211121@124.220.19.199:3306/t_ai
        # """
        # os.environ.setdefault("SGRID_CONFIG", yaml_text)
        if os.environ.get("SGRID_CONFIG"):
            print("Sgrid-Python[SGRID_CONFIG] Prod", True)
            conf = os.environ.get("SGRID_CONFIG")
            print("Sgrid-Python[conf]", conf)
            try:
                # bug修复：使用 load 函数代替 parse 函数
                config = load(conf, Loader=FullLoader)
                self.config = config
                print("Sgrid-Python[self.config]", self.config)
            except Exception as e:
                print(f"Sgrid-Python[Error] Failed to parse SGRID_CONFIG: {e}")
            return
        cwd = os.getcwd()
        # bug修复：将 cwd 转换为 Path 对象
        filepath = Path(cwd).joinpath(self.config_file)
        print("Sgrid-Python[read conf path]", filepath)
        with open(filepath, encoding="utf-8") as f:
            config = load(f, Loader=FullLoader)
            print("Sgrid-Python[conf] ==>", config)
            self.config = config

    # get ("server.port")
    def get(self, path, default=None):
        """
        :param path: 用点号分隔的键路径，例如 'a.b.c'
        :param default: 如果路径不存在，返回的默认值
        :return: 配置项的值，如果路径不存在则返回默认值
        """
        keys = path.split('.')
        current = self.config
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return default
        return current

    def get_port(self):
        if os.environ.get("SGRID_TARGET_PORT"):
            return int(os.environ.get("SGRID_TARGET_PORT"))
        return int(self.config.get("server.port", 8080))


