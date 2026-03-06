from HMAC.HMAC import hmac


def extract(salt:bytes, key:bytes):
    prk = hmac(salt,key)
    return prk
