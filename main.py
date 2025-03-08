import os

from conf import sgrid_config
from application import app
import uvicorn
from storage import test_add_chat_to_db

# def test():
#     if os.environ.get("SGRID_CONFIG"):
#         return True
#     test_add_chat_to_db()
#
# test()

def main():
    # 解析命令行参数
    port = sgrid_config.get_port()
    print(f"Sgrid-Python[load port] {port}")
    # 启动 uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)



if __name__ == "__main__":
    main()
