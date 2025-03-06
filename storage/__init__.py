from datetime import datetime
import random

from storage.storage import add_chat
import string


def test_add_chat_to_db():
    """
    测试添加聊天记录100万条
    :return:
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 循环100万次
    for i in range(1000000):
        # 这里需要根据 add_chat 函数的参数来传入合适的值
        # 假设 add_chat 函数需要 user_id, question, answer 等参数
        # 这里简单使用示例数据
        user_id = random.randint(0, 100)
        question = generate_random_text()
        answer = generate_random_text()
        add_chat(user_id, question, answer, random.randint(0, 2), random.randint(0, 2), now, random.randint(0, 1000))
        if i % 1000 == 0:
            print(f"已添加 {i} 条聊天记录")


def generate_random_text():
    """
    此函数用于随机生成 0 到 500 个字符的文本。
    :return: 随机生成的文本
    """
    # 定义所有可能的字符
    all_characters = string.ascii_letters + string.punctuation + string.whitespace
    # 随机确定文本长度
    length = random.randint(0, 500)
    # 生成随机文本
    random_text = ''.join(random.choice(all_characters) for _ in range(length))
    return random_text
