from hashlib import md5, sha512


def hash_512(raw_text):
    h = sha512()
    h.update(bytes(raw_text))
    return h.hexdigest()


def hash_md5(raw_text):
    h = md5()
    h.update(bytes(raw_text))
    return h.hexdigest()


from .user import *
from .confirmationlink import *
