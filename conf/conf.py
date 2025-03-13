import os
import signal
import sys

import uvicorn
from fastapi import FastAPI
from typing_extensions import Union

from yaml import load, FullLoader, parse
from pathlib import Path


class SgridConfig:
    config: Union[dict, None]

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
        sgrid_conf = os.environ.get("SGRID_CONFIG")
        if sgrid_conf:
            print("Sgrid-Python[SGRID_CONFIG] Prod", True)
            print("Sgrid-Python[conf]", sgrid_conf)
            try:
                config = load(sgrid_conf, Loader=FullLoader)
                self.config = config
                print("Sgrid-Python[self.config]", self.config)
            except Exception as e:
                print(f"Sgrid-Python[Error] Failed to parse SGRID_CONFIG: {e}")
            return
        cwd = os.getcwd()
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
        port = os.environ.get("SGRID_TARGET_PORT")
        if port:
            return int(port)
        if self.config is not None:
            return int(self.config.get("server.port", 8080))
        return 8080


class SgridApplication(SgridConfig):
    app: FastAPI = None
    server: uvicorn.Server = None

    def __init__(self, config_file="sgrid.yml"):
        super().__init__(config_file)

    async def run(self, app: FastAPI):
        # 解析命令行参数
        port = self.get_port()
        print(f"Sgrid-Python[load port] {port}")
        # 启动 uvicorn
        self.app = app
        uconf = uvicorn.Config(app, host="0.0.0.0", port=port)
        server = uvicorn.Server(uconf)
        try:
            self.wait_for_shutdown()
            await server.serve()
        except Exception as e:
            print(f"Sgrid-Python[Error] Failed to start server: {e}")

    def wait_for_shutdown(self):
        print("Sgrid-Python[wait_for_shutdown]")
        # 注册信号处理函数
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)

    def _signal_handler(self, sig, frame):
        print(f'Sgrid-Python[receive-signal-value] {sig}，shutdown。')
        self.server.shutdown()
        sys.exit(0)
