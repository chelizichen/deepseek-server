from application import app
from conf import sgrid_application
import asyncio

from storage import test_add_chat_to_db


# def test():
#     if os.environ.get("SGRID_CONFIG"):
#         return True
#     test_add_chat_to_db()
#
# test()


async def main():
    await sgrid_application.run(app=app)

if __name__ == "__main__":
    asyncio.run(main())
