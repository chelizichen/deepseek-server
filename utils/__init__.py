def wrap_response(data, message="success", code=0):
    """
    包装响应数据，返回包含 code, message, data 的结构体
    :param data: 响应的数据
    :param message: 响应消息，默认为 "success"
    :param code: 响应码，默认为 0
    :return: 包装后的响应结构体
    """
    return {
        "message": message,
        "data": data,
        "code": code
    }
