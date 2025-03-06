from storage.storage import user_login
from fernet import Fernet

# import os
# # 生成加密密钥
# KEY_FILE = 'encryption_key.key'
#
# # Generate and save the encryption key
# def generate_and_save_key():
#     key = Fernet.generate_key()
#     with open(KEY_FILE, 'wb') as key_file:
#         key_file.write(key)
#     return key
#
# # Load the encryption key
# def load_key():
#     if os.path.exists(KEY_FILE):
#         with open(KEY_FILE, 'rb') as key_file:
#             return key_file.read()
#     return generate_and_save_key()
#
# # Get the encryption key
key = "FMG7XdzNG5pdLMaFBgjt3S7mVEAO1hb5e3Gs-xDVr6Q=".encode()


# 加密函数
def encrypt_password(password):
    f = Fernet(key)
    encrypted = f.encrypt(password.encode())
    return encrypted


# 解密函数
def decrypt_password(encrypted_password):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_password).decode()
    return decrypted


def create_login_router(app):
    @app.get("/greet")
    async def root():
        return {"message": "Hello World"}

    @app.post("/user/login")
    async def login(data: dict):
        email = data.get("email")
        password = data.get("password")
        user = user_login(email)
        print(f"email: {email}, password: {password}, user.password: {user.password}")
        if user is not None:
            de_password = decrypt_password(user.password.encode())
            if de_password == password:
                return {"message": "Login successful", "user": user}
            return {"message": "Login failed, please check your email and password"}
        else:
            return {"message": "Login failed, please check your email and password"}
