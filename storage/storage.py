from conf.db import Session, User


# 用户增删改查功能
def add_user(name, email):
    session = Session()
    new_user = User(name=name, email=email)
    session.add(new_user)
    session.commit()
    user_dict = {
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email
    }
    session.close()
    return user_dict


def get_user(user_id):
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()
    session.close()
    return user


def update_user(user_id, name=None, email=None):
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        if name:
            user.name = name
        if email:
            user.email = email
        session.commit()
    session.close()
    return user


def delete_user(user_id):
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
    session.close()
    return user


if __name__ == "__main__":
    # 添加用户
    new_user = add_user("John Doe", "john@example.com")
    print(f"Added user: {new_user.id}, {new_user.name}, {new_user.email}")

    # 获取用户
    retrieved_user = get_user(new_user.id)
    print(f"Retrieved user: {retrieved_user.id}, {retrieved_user.name}, {retrieved_user.email}")

    # 更新用户
    updated_user = update_user(new_user.id, name="Jane Doe")
    print(f"Updated user: {updated_user.id}, {updated_user.name}, {updated_user.email}")

    # 删除用户
    deleted_user = delete_user(new_user.id)
    print(f"Deleted user: {deleted_user.id}, {deleted_user.name}, {deleted_user.email}")
