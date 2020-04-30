from hashlib import md5
import hmac
from hmac import new as hmac


def encrypt_md5(s):
    # 创建md5对象
    new_md5 = md5()
    # 这里必须用encode()函数对字符串进行编码，不然会报 TypeError: Unicode-objects must be encoded before hashing
    new_md5.update(s.encode(encoding='utf-8'))
    # 加密
    return new_md5.hexdigest()


def hash_hmac(ac_key, text):
    return str(hmac(ac_key, text, sha1).digest().encode('base64')[:-1])


# 调用
if __name__ == '__main__':
    print(encrypt_md5('admin'))