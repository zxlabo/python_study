# coding=utf-8

import hashlib


def md5(data):
    hash_md5 = hashlib.md5(data.encode('utf-8'))
    return hash_md5.hexdigest()


def sha1(data):
    hash_sha1 = hashlib.sha1(data.encode('utf-8'))
    return hash_sha1.hexdigest()
