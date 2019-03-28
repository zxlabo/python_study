# coding=utf-8

import json

from work.common import log


class LocationBaidu:
    status = -1  # 状态码：0为成功
    lat = 0.0  # 纬度值
    lng = 0.0  # 经度值
    precise = 0  # 位置的附加信息，是否精确查找。1为精确查找，即准确打点；0为不精确，即模糊打点
    confidence = 0  # 可信度，描述打点准确度，大于80表示误差小于100m。该字段仅作参考，返回结果准确度主要参考precise参数。
    level = ''  # 能精确理解的地址类型，包含：

    # UNKNOWN、国家、省、城市、区县、乡镇、村庄、道路、地产小区、商务大厦、政府机构、交叉路口、商圈、生活服务、
    # 休闲娱乐、餐饮、宾馆、购物、金融、教育、医疗、工业园区 、旅游景点 、汽车服务、火车站、长途汽车站、桥 、
    # 停车场/停车区、港口/码头、收费区/收费站、飞机场 、机场 、收费处/收费站 、加油站、绿地、门址

    def __init__(self, data):
        j = json.loads(data)
        if j is not None:
            self.status = j['status']
            if self.status != 0:
                return
            self.lat = j['result']['location']['lat']
            self.lng = j['result']['location']['lng']
            self.precise = j['result']['precise']
            self.confidence = j['result']['confidence']
            self.level = j['result']['level']

    def to_string(self):
        log.logd('[status:' + str(self.status) +
                 '][location:(lat)' + str(self.lat) + ' (lng)' + str(self.lng) +
                 '][precise:' + str(self.precise) +
                 '][confidence:' + str(self.confidence) +
                 '][level:' + self.level + ']')


class POIBaidu:
    status = 0
    message = ''
    total = 0
    results = []

    # noinspection PyBroadException
    def __init__(self, data):
        self.results = []
        try:
            j = json.loads(data)
            self.status = j['status']
            self.message = j['message']
            for r in j['results']:
                self.results.append(POIDetailBaidu(r))
            try:
                self.total = j['total']
            except Exception:
                self.total = len(self.results)
        except Exception:
            pass


class POIDetailBaidu:
    name = ''
    lat = 0.0
    lng = 0.0
    address = ''
    province = ''
    city = ''
    area = ''
    detail = 0
    uid = ''
    distance = 0

    trans_type = 0  # 1-地铁站；2-公交站；3-地铁线；4-公交线

    # noinspection PyBroadException
    def __init__(self, data):
        if data is not None:
            try:
                self.name = data['name']
            except Exception:
                pass
            try:
                self.lat = data['location']['lat']
                self.lng = data['location']['lng']
            except Exception:
                pass
            try:
                self.address = data['address']
            except Exception:
                pass
            try:
                self.province = data['province']
                self.city = data['city']
                self.area = data['area']
                self.detail = data['detail']
                self.uid = data['uid']
            except Exception:
                pass
            try:
                self.distance = data['detail_info']['distance']
            except Exception:
                pass


class CityL2:
    id = 0
    pid = 0
    short_name = ''
    name = ''
    level = 0
    districts = {}

    def __init__(self, data):
        self.id = int(data[0])
        self.pid = int(data[1])
        self.short_name = str(data[2])
        self.name = str(data[3])
        self.level = int(data[4])
        self.districts = {}


class DistrictL2:
    id = 0
    pid = 0
    shortname = ''
    name = ''
    level = 0
    code = ''
    zip = ''
    alias = []
    region_house = None
    business_map = None

    def __init__(self):
        self.alias = []

    def fill(self, data):
        self.id = int(data[0])
        self.pid = int(data[1])
        self.shortname = data[2]
        self.name = data[3]
        self.level = int(data[4])
        self.code = data[5]
        self.zip = data[6]
        if data[7]:
            self.alias = data[7].split(',')

    def is_real(self):
        return self.zip is not None and len(self.zip) > 0

    def valid(self):
        return self.id != 0


class BusinessL2:
    id = 0
    business_name = ''
    city_id = 0
    district_id = 0
    update_time = ''
    create_time = ''
    business_region_house = None

    def __init__(self):
        pass

    def fill(self, data):
        self.id = int(data[0])
        self.business_name = str(data[1])
        self.city_id = int(data[2])
        self.district_id = int(data[3])
        self.update_time = str(data[4])
        self.create_time = str(data[5])

    def fill_business(self, data):
        self.id = int(data[0])
        self.business_name = str(data[1])
        self.city_id = int(data[2])
        self.district_id = int(data[3])

    def to_string(self):
        log.logd('[id:' + str(self.id) +
                 '][business_name:' + str(self.business_name) +
                 '][city_id:' + str(self.city_id) +
                 '][district_id:' + str(self.district_id) + ']')


class TransportL2:
    id = 0
    parent_id = ''
    trans_type = 0
    trans_name = ''
    level = 0
    city_id = 0
    district_id = 0
    latitude = ''
    longtitude = ''
    updatetime = ''
    createtime = ''

    def fill_with_db(self, data):
        self.id = int(data[0])
        self.parent_id = str(data[1])
        self.trans_type = int(data[2])
        self.trans_name = str(data[3])
        self.level = int(data[4])
        self.city_id = int(data[5])
        self.district_id = int(data[6])
        self.latitude = str(data[7])
        self.longtitude = str(data[8])
        self.updatetime = str(data[9])
        self.createtime = str(data[10])

    def fill_with_poi(self, poi):
        self.trans_name = poi.name
        self.latitude = poi.lat
        self.longtitude = poi.lng
        self.trans_type = poi.trans_type


class TileL2:
    id = 0
    hash_tile = ''
    tile_x = 0
    tile_y = 0
    business_id = 0
    update_time = 0
    create_time = 0

    def fill_with_db(self, data):
        if data is None:
            return
        self.id = int(data[0])
        self.hash_tile = data[1]
        self.tile_x = int(data[2])
        self.tile_y = int(data[3])
        self.business_id = int(data[4])
        self.create_time = int(data[5])
        self.update_time = int(data[6])

    def valid(self):
        return isinstance(self.hash_tile, str) and self.business_id > 0
