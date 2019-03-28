# coding=utf-8

import pymysql

from work.common import config


def connect_admin_db():
    configs = config.load_config(['db_host_admin', 'db_user_admin', 'db_pwd_admin'])
    db_host = configs['db_host_admin']
    db_user = configs['db_user_admin']
    db_pwd = configs['db_pwd_admin']
    return pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_pwd,
        database='gyj_admin',
        charset='utf8',
        read_timeout=60,
        write_timeout=60)


def connect_pontus_db():
    configs = config.load_config(['db_host_pontus', 'db_user_pontus', 'db_pwd_pontus'])
    db_host = configs['db_host_pontus']
    db_user = configs['db_user_pontus']
    db_pwd = configs['db_pwd_pontus']
    return pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_pwd,
        database='gyj_pontus',
        charset='utf8',
        read_timeout=60,
        write_timeout=60)


def connect_spider_db():
    configs = config.load_config(['db_host_spider', 'db_user_spider', 'db_pwd_spider'])
    db_host = configs['db_host_spider']
    db_user = configs['db_user_spider']
    db_pwd = configs['db_pwd_spider']
    return pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_pwd,
        database='gyj_house',
        charset='utf8',
        read_timeout=60,
        write_timeout=60)
