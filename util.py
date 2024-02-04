import os

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import zlib
import json
from env import EncryptKey


class Encrypt:
    def __init__(self, key, bs=32):
        key = key + (bs - len(key)) * "\0"
        self.key = key.encode('utf-8')

    def aes_decrypt(self, content):
        text = base64.b64decode(content)
        iv = text[0:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(base64.b64decode(text[16:]))
        return unpad(decrypted, AES.block_size).decode('utf-8', errors='ignore')


encrypt = Encrypt(key=EncryptKey)


def decrypt(request):
    req_data: str = zlib.decompress(request.get_data()).decode("utf-8")
    req_data: dict = json.loads(req_data)
    data: str = encrypt.aes_decrypt(req_data["encrypt"])
    data: dict = json.loads(data)
    data: dict = data["d"]
    return data
