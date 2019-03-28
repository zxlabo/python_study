# coding=utf-8

import math
import re
import urllib.parse
import hashlib
import urllib3
import json

from work.model.area import LocationBaidu, POIBaidu
from work.common import log

x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 扁率

# 地铁正则
metro_re = {2: ['地铁[0-9]+号线'],  # 北京
            802: ['地铁[0-9]+号线'],  # 上海
            1965: ['地铁[0-9]+号线'],  # 广州
            1988: ['[0-9]+号线'],  # 深圳
            2368: ['地铁[0-9]+号线'],  # 成都
            934: ['地铁[0-9]+号线'],  # 杭州
            1710: ['地铁[0-9]+号线'],  # 武汉
            821: ['地铁[0-9]+号线'],  # 南京
            20: ['地铁[0-9]+号线', '津滨[0-9]+号线'],  # 天津
            }
# 公交正则
bus_re = {2: ['[a-z0-9]+路', '[a-z0-9]+路区间', '夜[a-z0-9]+路', '[a-z0-9]+路快车'],  # 北京
          802: ['[a-z0-9]+路', '[\u4e00-\u9fa5]+[a-z0-9]+路'],  # 上海
          1965: ['[a-z0-9]+路'],  # 广州
          1988: ['[a-z0-9]+路', '[a-z0-9]+区间线', '前海行[a-z0-9]+路'],  # 深圳
          2368: ['[a-z0-9]+路', '[\u4e00-\u9fa5]+[a-z0-9]+路'],  # 成都
          934: ['[a-z0-9]+路', '[a-z0-9]+路区间', '[a-z0-9]+支[a-z0-9]+路'],  # 杭州
          1710: ['[a-z0-9]+路'],  # 武汉
          821: ['[a-z0-9]+路', '[a-z0-9]+路夜间'],  # 南京
          20: ['[a-z0-9]+路', '[a-z0-9]+路区间', '通勤快车[a-z0-9]+路', '校线[a-z0-9]+路', '[a-z0-9]+路高峰线',
               '[a-z0-9]+路大圈', '[a-z0-9]+路晚高峰', '东丽开发区[a-z0-9]+路'],  # 天津
          }

lbs_ak_bk1 = 'IiCd9t5SjRfQQkkDzuLg0tDw0nwlHNGx'
lbs_sk_bk1 = 'L1nMnGZfxEQ5eNnVGCZ0fytUor7Ydx8u'

lbs_ak = 'uGYTT2KWzbbGi3m7E9zKfU6DbiyuAqaA'
lbs_sk = 'HfumOwoCydWFeb8aGfXxRZppuEFf2I0x'


# 根据地址信息请求百度地图坐标位置
def request_baidu_location(addr):
    location = do_request_baidu_location(addr)
    if location.status == 302:
        global lbs_ak
        global lbs_sk
        lbs_ak = lbs_ak_bk1
        lbs_sk = lbs_sk_bk1
        log.log('func request_baidu_location change key')
    return do_request_baidu_location(addr)


def do_request_baidu_location(addr):
    query_str = '/geocoder/v2/?address=%s&output=json&ak=%s' % (addr, lbs_ak)
    encoded_str = urllib.parse.quote(query_str, safe="/:=&?#+!$,;'@()*[]")
    raw_str = encoded_str + lbs_sk
    hash_str = hashlib.md5(urllib.parse.quote_plus(raw_str).encode('utf-8')).hexdigest()
    req = 'http://api.map.baidu.com' + encoded_str + '&sn=' + hash_str
    conn = urllib3.PoolManager()
    ret = conn.request('GET', req)
    return LocationBaidu(ret.data)


def do_request_baidu_address(lat, lng):
    query_str = '/geocoder/v2/?location=%f,%f&output=json&pois=1&latest_admin=1&ak=%s' % (
        lat, lng, lbs_ak)
    encoded_str = urllib.parse.quote(query_str, safe="/:=&?#+!$,;'@()*[]")
    raw_str = encoded_str + lbs_sk
    hash_str = hashlib.md5(urllib.parse.quote_plus(raw_str).encode('utf-8')).hexdigest()
    req = 'http://api.map.baidu.com' + encoded_str + '&sn=' + hash_str
    conn = urllib3.PoolManager()
    ret = conn.request('GET', req)
    j = json.loads(ret.data)
    print(json.dumps(j))
    # return LocationBaidu(ret.data)


# 根据经纬度信息请求百度的POI信息
def request_baidu_poi(lat, lng, page_num):
    poi = do_request_baidu_poi(lat, lng, page_num)
    if poi.status == 302:
        global lbs_ak
        global lbs_sk
        lbs_ak = lbs_ak_bk1
        lbs_sk = lbs_sk_bk1
        log.log('func request_baidu_poi change key')
    return do_request_baidu_poi(lat, lng, page_num)


def do_request_baidu_poi(lat, lng, page_num):
    query_str = "/place/v2/search?query=地铁站$公交车站&location=%f,%f&tag=地铁站,公交车站" \
                "&radius=800&output=json&scope=2&page_num=%d&page_size=20&ak=%s" \
                % (lat, lng, page_num, lbs_ak)
    encoded_str = urllib.parse.quote(query_str, safe="/:=&?#+!$,;'@()*[]")
    raw_str = encoded_str + lbs_sk
    hash_str = hashlib.md5(urllib.parse.quote_plus(raw_str).encode('utf-8')).hexdigest()
    req = 'http://api.map.baidu.com' + encoded_str + '&sn=' + hash_str
    conn = urllib3.PoolManager()
    ret = conn.request('GET', req)
    j = json.loads(ret.data)
    print(json.dumps(j))
    return POIBaidu(ret.data)


# 判断是否是地铁或公交
def is_transport_addr(poi, city_id):
    if poi is not None and poi.address:
        trans_list = poi.address.split(';')
        for t in trans_list:
            if city_id in metro_re:
                pattern = metro_re[city_id]
                for p in pattern:
                    if re.match(p, t, 0):
                        poi.trans_type = 1
                        return True
            if city_id in bus_re:
                pattern = bus_re[city_id]
                for p in pattern:
                    if re.match(p, t, 0):
                        poi.trans_type = 2
                        return True
    return False


def gcj02tobd09(lng, lat):
    """
    火星坐标系(GCJ-02)转百度坐标系(BD-09)
    谷歌、高德——>百度
    :param lng:火星坐标经度
    :param lat:火星坐标纬度
    :return:
    """
    z = math.sqrt(lng * lng + lat * lat) + 0.00002 * math.sin(lat * x_pi)
    theta = math.atan2(lat, lng) + 0.000003 * math.cos(lng * x_pi)
    bd_lng = z * math.cos(theta) + 0.0065
    bd_lat = z * math.sin(theta) + 0.006
    return [bd_lng, bd_lat]


def bd09togcj02(bd_lon, bd_lat):
    """
    百度坐标系(BD-09)转火星坐标系(GCJ-02)
    百度——>谷歌、高德
    :param bd_lat:百度坐标纬度
    :param bd_lon:百度坐标经度
    :return:转换后的坐标列表形式
    """
    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
    gg_lng = z * math.cos(theta)
    gg_lat = z * math.sin(theta)
    return [gg_lng, gg_lat]


def wgs84togcj02(lng, lat):
    """
    WGS84转GCJ02(火星坐标系)
    :param lng:WGS84坐标系的经度
    :param lat:WGS84坐标系的纬度
    :return:
    """
    if out_of_china(lng, lat):  # 判断是否在国内
        return lng, lat
    dlat = transformlat(lng - 105.0, lat - 35.0)
    dlng = transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [mglng, mglat]


def gcj02towgs84(lng, lat):
    """
    GCJ02(火星坐标系)转GPS84
    :param lng:火星坐标系的经度
    :param lat:火星坐标系纬度
    :return:
    """
    if out_of_china(lng, lat):
        return lng, lat
    dlat = transformlat(lng - 105.0, lat - 35.0)
    dlng = transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [lng * 2 - mglng, lat * 2 - mglat]


def transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
          0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret


def transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
          0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *
            math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
            math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret


def out_of_china(lng, lat):
    """
    判断是否在国内，不在国内不做偏移
    :param lng:
    :param lat:
    :return:
    """
    if lng < 72.004 or lng > 137.8347:
        return True
    if lat < 0.8293 or lat > 55.8271:
        return True
    return False
