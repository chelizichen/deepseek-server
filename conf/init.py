import os

from yaml import load, FullLoader, parse
from pathlib import Path


class SgridConfig:
    def __init__(self, config_file="sgrid.yml"):
        self.config = None
        self.config_file = config_file

    def init_config(self):
        if os.environ.get("SGRID_CONFIG"):
            print("Sgrid-Python[SGRID_CONFIG] Prod", True)
            conf = os.environ.get("SGRID_CONFIG")
            print("Sgrid-Python[conf]", conf)
            config = parse(conf, Loader=FullLoader)
            self.config = config
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


sgrid_config = SgridConfig()
sgrid_config.init_config()
