from Passwords.generator import generate
from PBKDF2.PBKDF2 import pbkdf2
import json
import time


def password_storage(name,key):
    salt = generate(128)
    b_key = key.encode('utf-8')

    with open("Passwords/storage.json", "r") as f:
        data = json.load(f)

    encrypted = pbkdf2(b_key, salt, 100000, len(b_key))

    store = {
                "Username": name,
                "Salt": salt.hex(),
                "Hash": encrypted.hex()
                }

    data[f"record{len(data)}"] = store

    with open("Passwords/storage.json", "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

