import  uuid
"""
chat_type_common 正常类型
chat_type_common 2 摘要类型
"""
chat_type_common = 1
chat_type_abstract = 2

"""
answer_type_common 1 普通类型
answer_type_common 2 推荐类型
answer_type_common 3 不推荐类型
"""
answer_type_common = 1
answer_type_like = 2
answer_type_dislike = 3

session_delete = -1

# lock
chat_lock = 1
chat_unlock = 2

# 定义命名空间
NAME_SPACE = "chat"


def new_uuid():
    namespace = uuid.NAMESPACE_DNS
    uuid3_str = str(uuid.uuid3(namespace, NAME_SPACE))
    return uuid3_str