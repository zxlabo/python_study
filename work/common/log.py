# coding=utf-8

import time
import datetime

# debug操作日志
debug = False
# 房源清洗操作日志
debug1 = False
# 房源聚类操作日志
debug2 = False
# 图片上传操作日志
debug3 = False
# 自平台数据同步操作日志
debug4 = False
# 自平台图片上传操作日志
debug5 = False
# Metis分析平台
debug6 = False


def log(msg):
    print('[%s] %s' % (now(), msg))


def logd(msg):
    if debug:
        print('[%s] %s' % (now(), msg))


def logd1(msg):
    if debug1:
        print('[%s] %s' % (now(), msg))


def logd2(msg):
    if debug2:
        print('[%s] %s' % (now(), msg))


def logd3(msg):
    if debug3:
        print('[%s] %s' % (now(), msg))


def logd4(msg):
    if debug4:
        print('[%s] %s' % (now(), msg))


def logd5(msg):
    if debug5:
        print('[%s] %s' % (now(), msg))


def logd6(msg):
    if debug6:
        print('[%s] %s' % (now(), msg))


def error(msg):
    print('[%s][ERROR] %s' % (now(), msg))


def now():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def default_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(0))


def convert_to_datetime(ut):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ut))


def today():
    return datetime.date.today()


def previous_datetime(last):
    t = datetime.datetime.today()
    oneday = datetime.timedelta(days=last)
    return t - oneday


def convert_to_unixtime(st):
    try:
        return int(time.mktime(time.strptime(st, '%Y-%m-%d %H:%M:%S')))
    except Exception as e:
        error('func convert_to_unixtime handle exception\n%s' % repr(e))
        return 0
