# coding=utf-8
import datetime
import re

from common import lbs, hash, log
from l2 import db_l2, tool_l2
from l3 import tool_l3
from model.area import TransportL2, TileL2
from model.community import CommunityL2
from model.record import Locus


# 房屋室内外设施数据
class HouseDevice:
    id = 0
    device_type = 0  # 1-室内设施；2-公共设施
    device_name = ''  # 设备名称
    device_icon = ''  # 设备图标
    other_name = ''  # 别名
    idx = 0

    # noinspection PyBroadException
    def __init__(self, data):
        self.id = int(data[0])
        self.device_type = int(data[1])
        self.device_name = str(data[2])
        try:
            self.device_icon = int(data[3])
        except Exception:
            pass
        try:
            self.other_name = str(data[4])
        except Exception:
            pass
        self.idx = int(data[5])


# L1级库房源信息数据
class HouseL1:
    house_id = ''
    house_name = ''
    city_name = ''
    district_name = ''
    business_name = ''
    house_url = ''
    house_type = ''
    community_id = 0
    address = ''
    house_desc = ''
    on_floor = ''
    total_floor = ''
    building = ''
    room_number = ''
    building_area = 0.0
    room = 0
    living = 0
    washing = 0
    cook = 0
    balcony = 0
    latitude = 0.0
    longtitude = 0.0
    rent_mode = 0
    rent_period = 0
    direction = ''
    price = 0.0
    price_detail = ''
    service_fee = ''
    commission_price = 0.0
    brand_name = ''
    deposit_type = 0.0
    status = 0
    src_type = 0
    user_name = ''
    user_phone = ''
    user_type = 0
    pay_type = 0
    transport_tag = ''
    tag = ''
    device_tag = ''
    service_tag = ''
    release_time = ''
    create_time = ''
    update_time = ''
    hashStr = ''
    scrapy_time = ''
    decoration_type = 0
    heating_mode = 0
    community_name = ''
    remark = ''

    def __init__(self):
        pass

    def self_check(self):
        if isinstance(self.house_id, str):
            self.house_id = self.house_id.strip()
        else:
            self.house_id = ''
        if isinstance(self.house_name, str):
            self.house_name = self.house_name.strip()
        else:
            self.house_name = ''
        if isinstance(self.city_name, str):
            self.city_name = self.city_name.strip()
        else:
            self.city_name = ''
        if isinstance(self.district_name, str) and len(self.district_name) > 0:
            self.district_name = self.district_name.strip()
        else:
            self.district_name = '其它'
        if isinstance(self.business_name, str) and len(self.business_name) > 0:
            self.business_name = self.business_name.strip()
        else:
            self.business_name = '其它'
        if isinstance(self.house_url, str):
            self.house_url = self.house_url.strip()
        else:
            self.house_url = ''
        if isinstance(self.house_type, str):
            self.house_type = self.house_type.strip()
        else:
            self.house_type = ''
        if isinstance(self.address, str):
            self.address = self.address.strip()
        else:
            self.address = ''
        if isinstance(self.house_desc, str):
            self.house_desc = self.house_desc.strip()
        else:
            self.house_desc = ''
        if isinstance(self.on_floor, str):
            self.on_floor = self.on_floor.strip()
        else:
            self.on_floor = ''
        if isinstance(self.total_floor, str):
            self.total_floor = self.total_floor.strip()
        else:
            self.total_floor = ''
        if isinstance(self.building, str):
            self.building = self.building.strip()
        else:
            self.building = ''
        if isinstance(self.room_number, str):
            self.room_number = self.room_number.strip()
        else:
            self.room_number = ''
        if self.building_area < 0.0:
            self.building_area = 0.0
        if self.room < 0:
            self.room = 0
        if self.living < 0:
            self.living = 0
        if self.washing < 0:
            self.washing = 0
        if self.cook < 0:
            self.cook = 0
        if self.balcony < 0:
            self.balcony = 0
        if self.latitude < 0.0:
            self.latitude = 0.0
        if self.longtitude < 0.0:
            self.longtitude = 0.0
        if self.rent_mode < 0:
            self.rent_mode = 0
        if self.rent_period < 0:
            self.rent_period = 0
        if isinstance(self.direction, str):
            self.direction = self.direction.strip()
        else:
            self.direction = '0000'
        if self.price < 0:
            self.price = 0
        if isinstance(self.price_detail, str):
            self.price_detail = self.price_detail.strip()
        else:
            self.price_detail = '0|0|0|0|0'
        if isinstance(self.service_fee, str):
            self.service_fee = self.service_fee.strip()
        else:
            self.service_fee = '0|0|0|0|0'
        if self.commission_price < 0.0:
            self.commission_price = 0.0
        if isinstance(self.brand_name, str):
            self.brand_name = self.brand_name.strip()
        else:
            self.brand_name = ''
        if self.deposit_type < 0.0:
            self.deposit_type = 0.0
        if isinstance(self.user_name, str):
            self.user_name = self.user_name.strip()
        else:
            self.user_name = ''
        if isinstance(self.user_phone, str):
            self.user_phone = self.user_phone.strip()
        else:
            self.user_phone = ''
        if isinstance(self.transport_tag, str):
            self.transport_tag = self.transport_tag.strip()
        else:
            self.transport_tag = ''
        if isinstance(self.tag, str):
            self.tag = self.tag.strip()
        else:
            self.tag = ''
        if isinstance(self.device_tag, str):
            self.device_tag = self.device_tag.strip()
        else:
            self.device_tag = ''
        if isinstance(self.service_tag, str):
            self.service_tag = self.service_tag.strip()
        else:
            self.service_tag = ''
        if not isinstance(self.create_time, datetime.datetime):
            self.create_time = log.default_time()
        if not isinstance(self.release_time, datetime.datetime):
            self.release_time = log.default_time()
        if not isinstance(self.update_time, datetime.datetime):
            self.update_time = log.default_time()
        if not isinstance(self.scrapy_time, datetime.datetime):
            self.scrapy_time = log.default_time()
        if isinstance(self.hashStr, str):
            self.hashStr = self.hashStr.strip()
        else:
            self.hashStr = ''
        if self.deposit_type < 0:
            self.deposit_type = 0
        if isinstance(self.community_name, str):
            self.community_name = self.community_name.strip()
        else:
            self.community_name = ''
        if isinstance(self.remark, str):
            self.remark = self.remark.strip()
        else:
            self.remark = ''

    # 填入简单信息，包含hashStr字段和爬取时间
    def fill_simple(self, data):
        self.house_id = data[0]
        self.hashStr = data[1]
        self.scrapy_time = data[2]
        try:
            self.status = int(data[3])
        except Exception:
            self.status = 0
        self.self_check()

    # 填入全量数据
    # noinspection PyBroadException
    def fill_all(self, data):
        self.house_id = data[0]
        self.house_name = data[1]
        self.city_name = data[2]
        self.district_name = data[3]
        self.business_name = data[4]
        self.house_url = data[5]
        self.house_type = data[6]
        try:
            self.community_id = int(data[7])
        except Exception:
            pass
        self.address = data[8]
        self.house_desc = data[9]
        self.on_floor = data[10]
        self.total_floor = data[11]
        self.building = data[12]
        self.room_number = data[13]
        try:
            self.building_area = float(data[14])
        except Exception:
            pass
        # 跳过layout
        try:
            self.room = int(data[16])
        except Exception:
            pass
        try:
            self.living = int(data[17])
        except Exception:
            pass
        try:
            self.washing = int(data[18])
        except Exception:
            pass
        try:
            self.cook = int(data[19])
        except Exception:
            pass
        try:
            self.balcony = int(data[20])
        except Exception:
            pass
        try:
            self.latitude = float(data[21])
        except Exception:
            pass
        try:
            self.longtitude = float(data[22])
        except Exception:
            pass
        try:
            self.rent_mode = int(data[23])
        except Exception:
            pass
        try:
            self.rent_period = int(data[24])
        except Exception:
            pass
        self.direction = data[25]
        try:
            self.price = float(data[26])
        except Exception:
            pass
        self.price_detail = data[27]
        self.service_fee = data[28]
        try:
            self.commission_price = float(data[29])
        except Exception:
            pass
        self.brand_name = data[30]
        try:
            self.deposit_type = float(data[31])
        except Exception:
            pass
        try:
            self.status = int(data[32])
        except Exception:
            pass
        try:
            self.src_type = int(data[33])
        except Exception:
            pass
        self.user_name = data[34]
        self.user_phone = data[35]
        try:
            self.user_type = int(data[36])
        except Exception:
            pass
        try:
            self.pay_type = int(data[37])
        except Exception:
            pass
        self.transport_tag = data[38]
        self.tag = data[39]
        self.device_tag = data[40]
        self.service_tag = data[41]
        self.release_time = data[42]
        self.create_time = data[43]
        self.update_time = data[44]
        self.hashStr = data[45]
        self.scrapy_time = data[46]
        try:
            self.decoration_type = int(data[47])
        except Exception:
            pass
        try:
            self.heating_mode = int(data[48])
        except Exception:
            pass
        self.community_name = data[49]
        self.remark = data[50]
        self.self_check()

    def valid(self):
        return len(self.city_name) > 0 and len(self.district_name) > 0 and len(self.house_id) > 0 \
               and self.price > 0 and len(self.hashStr) > 0


# L2级库房源信息数据
class HouseL2:
    # ---采集库字段---
    house_uid = ''
    third_house_id = ''
    city_id = 0
    district_id = 0
    business_id_v2 = 0
    house_name = ''
    house_url = ''
    house_type = ''
    community_id_v2 = ''
    community_name = ''
    address = ''
    house_desc = ''
    on_floor = ''
    total_floor = ''
    building = ''
    room_number = ''
    building_area = 0.0
    room = 0
    living = 0
    washing = 0
    cook = 0
    balcony = 0
    latitude = 0.0
    longtitude = 0.0
    rent_mode = 0
    rent_period = 0
    direction = ''
    price = 0.0
    price_detail = ''
    service_fee = ''
    commission_price = 0.0
    brand_name_sp = ''
    brand_id_sp = 0
    deposit_type = 0.0
    status = 0
    src_type = 0
    user_name = ''
    user_phone = ''
    user_type = 0
    pay_type = 0
    device_id = ''
    service_id = ''
    decoration_type = ''
    bus_id = ''
    bus_desc = ''
    metro_id = ''
    metro_desc = ''
    tag = ''
    create_time = ''
    update_time = ''
    scrapy_time = ''
    hashStr = ''
    hash_img = ''
    version = 0
    house_oid = 0
    tile_x = 0
    tile_y = 0

    # ---自有房源字段---
    brand_name = ''
    brand_id = 0
    tenant = 0
    landlord = 0

    # ---非数据库字段---
    # 房源特征hash，以房源固定特征为准计算hash，用以同条件房源聚类
    hash_feture = ''
    hash_feture_self = ''
    # 房源特征level，以房源非固定特征为准计算hash，用以同条件房源聚类
    level_feture = ''
    level_feture_self = ''
    # 房源瓦片hash
    hash_tile = ''
    # 采集库中的在租状态与L2库中的在租状态不同
    status_diff = False
    # 关联的l3_relative_id
    relative_id = 0
    # 中间状态相关的标记位
    flag_locus = 0  # 是否有轨迹变化，决定是否要录入轨迹信息

    def __init__(self):
        pass

    def fill_with_db_relative(self, data):
        self.house_uid = data[0]
        self.relative_id = int(data[1])
        self.metro_desc = data[2]
        self.price = float(data[3])
        self.src_type = int(data[4])
        self.community_id_v2 = data[5]
        self.user_phone = data[6]
        self.room = int(data[7])
        self.business_id_v2 = int(data[8])
        self.hash_img = data[9]

    def fill_with_db_cluster(self, data):
        self.house_uid = data[0]
        self.community_name = data[1]
        self.room = int(data[2])
        self.living = int(data[3])
        self.washing = int(data[4])
        self.cook = int(data[5])
        self.balcony = int(data[6])
        self.building_area = float(data[7])
        self.direction = data[8]
        self.on_floor = data[9]
        self.total_floor = data[10]
        self.device_id = data[11]
        self.business_id_v2 = int(data[12])
        self.latitude = float(data[13])
        self.longtitude = float(data[14])
        self.rent_period = int(data[15])
        self.house_oid = int(data[16])

    def fill_with_db_simple(self, data):
        self.house_uid = data[0]
        self.hashStr = data[1]
        self.scrapy_time = data[2]
        self.status = int(data[3])
        self.price = float(data[4])
        self.room = int(data[5])
        self.business_id_v2 = int(data[6])

    def fill_with_db_hash_img(self, data):
        self.house_uid = data[0]
        self.third_house_id = data[1]
        self.hash_img = data[2]

    def fill_with_db_self_simple(self, data):
        self.house_uid = str(data[0])
        self.hashStr = data[1]
        self.third_house_id = str(data[2])
        self.hash_img = data[3]
        self.src_type = int(data[4])
        self.district_id = int(data[5])
        self.business_id_v2 = int(data[6])
        self.latitude = float(data[7])
        self.longtitude = float(data[8])
        self.price = float(data[9])
        self.status = int(data[10])
        self.metro_desc = data[11]
        self.user_phone = data[12]
        self.community_id_v2 = data[13]

    def fill_with_db(self, data):
        self.house_uid = data[0]
        self.third_house_id = data[1]
        self.city_id = int(data[2])
        self.district_id = int(data[3])
        self.business_id_v2 = int(data[4])
        self.house_name = data[5]
        self.house_url = data[6]
        self.house_type = data[7]
        self.community_id_v2 = data[8]
        self.community_name = data[9]
        self.address = data[10]
        self.house_desc = data[11]
        self.on_floor = data[12]
        self.total_floor = data[13]
        self.building = data[14]
        self.room_number = data[15]
        self.building_area = float(data[16])
        self.room = int(data[17])
        self.living = int(data[18])
        self.washing = int(data[19])
        self.cook = int(data[20])
        self.balcony = int(data[21])
        self.latitude = float(data[22])
        self.longtitude = float(data[23])
        self.rent_mode = int(data[24])
        self.rent_period = int(data[25])
        self.direction = data[26]
        self.price = float(data[27])
        self.price_detail = data[28]
        self.service_fee = data[29]
        self.commission_price = float(data[30])
        self.brand_name_sp = data[31]
        self.brand_id_sp = int(data[32])
        self.deposit_type = float(data[33])
        self.status = int(data[34])
        self.src_type = int(data[35])
        self.user_name = data[36]
        self.user_phone = data[37]
        self.user_type = int(data[38])
        self.pay_type = int(data[39])
        self.device_id = data[40]
        self.service_id = data[41]
        self.decoration_type = data[42]
        self.bus_id = data[43]
        self.bus_desc = data[44]
        self.metro_id = data[45]
        self.metro_desc = data[46]
        self.tag = data[47]
        self.create_time = data[48]
        self.update_time = data[49]
        self.scrapy_time = data[50]
        self.hashStr = data[51]
        self.hash_img = data[52]
        self.version = int(data[53])
        self.house_oid = int(data[54])
        self.tile_x = int(data[55])
        self.tile_y = int(data[56])

    def fill_with_old_db(self, data):
        self.house_uid = data[0]
        self.third_house_id = data[1]
        self.city_id = int(data[2])
        self.district_id = int(data[3])
        self.latitude = float(data[4])
        self.longtitude = float(data[5])
        self.bus_id = data[6]
        self.bus_desc = data[7]
        self.metro_id = data[8]
        self.metro_desc = data[9]
        self.hash_img = data[10]
        self.version = int(data[11])

    def fill_with_self_db(self, data):
        self.house_uid = data[0]
        self.city_id = int(data[1])
        self.district_id = int(data[2])
        self.business_id_v2 = int(data[3])
        self.house_name = data[4]
        self.house_url = data[5]
        self.house_type = data[6]
        self.community_id_v2 = data[7]
        self.community_name = data[8]
        self.address = data[9]
        self.house_desc = data[10]
        self.on_floor = data[11]
        self.total_floor = data[12]
        self.building = data[13]
        self.room_number = data[14]
        self.building_area = float(data[15])
        self.room = int(data[16])
        self.living = int(data[17])
        self.washing = int(data[18])
        self.cook = int(data[19])
        self.balcony = int(data[20])
        self.latitude = float(data[21])
        self.longtitude = float(data[22])
        self.rent_mode = int(data[23])
        self.rent_period = int(data[24])
        self.direction = data[25]
        self.price = float(data[26])
        self.price_detail = data[27]
        self.service_fee = data[28]
        self.commission_price = float(data[29])
        self.brand_name = data[30]
        self.brand_id = int(data[31])
        self.deposit_type = float(data[32])
        self.status = int(data[33])
        self.src_type = int(data[34])
        self.user_type = int(data[35])
        self.pay_type = int(data[36])
        self.device_id = data[37]
        self.service_id = data[38]
        self.bus_id = data[39]
        self.bus_desc = data[40]
        self.tag = data[41]
        self.metro_desc = data[42]
        self.metro_id = data[43]
        self.create_time = data[44]
        self.update_time = data[45]
        self.hashStr = data[46]
        self.decoration_type = data[47]
        self.version = int(data[48])
        self.hash_img = data[49]
        self.house_oid = int(data[50])
        self.landlord = int(data[51])
        self.tenant = int(data[52])
        self.user_name = str(data[54])
        self.user_phone = str(data[55])
        self.third_house_id = data[56]

    # 使用L1级简要版数据填充
    def fill_with_l1_simple(self, h_l1_simple, cid, did):
        self.third_house_id = h_l1_simple.house_id
        self.hashStr = h_l1_simple.hashStr
        self.scrapy_time = h_l1_simple.scrapy_time
        self.src_type = h_l1_simple.src_type
        self.status = h_l1_simple.status
        self.city_id = cid
        self.district_id = did

    # 使用L1级全量数据填充
    def fill_with_l1_full(self, h_l1, city_id, dist_id, device_list):
        if not isinstance(h_l1, HouseL1) or not h_l1.valid():
            return False
        self.third_house_id = h_l1.house_id
        self.city_id = city_id
        self.district_id = dist_id
        if not isinstance(self.house_uid, str) or len(self.house_uid) == 0:
            # 检查house uid
            self.hash_house_uid()
        # self.business_id_v2 由update business填写
        self.house_name = h_l1.house_name
        self.house_url = h_l1.house_url
        self.house_type = h_l1.house_type
        # self.community_id_v2 由update community填写
        self.community_name = h_l1.community_name
        self.address = h_l1.address
        self.house_desc = h_l1.house_desc
        self.on_floor = h_l1.on_floor
        self.total_floor = h_l1.total_floor
        self.building = h_l1.building
        self.room_number = h_l1.room_number
        self.building_area = h_l1.building_area
        self.room = h_l1.room
        self.living = h_l1.living
        self.washing = h_l1.washing
        self.cook = h_l1.cook
        self.balcony = h_l1.balcony
        self.latitude = h_l1.latitude
        self.longtitude = h_l1.longtitude
        self.rent_mode = h_l1.rent_mode
        self.rent_period = h_l1.rent_period
        self.direction = h_l1.direction
        self.price_detail = h_l1.price_detail
        # 对价格进行最低价和最高价的计算
        self.price = tool_l2.convert_price(h_l1.price_detail, h_l1.price)[0]
        self.service_fee = h_l1.service_fee
        try:
            self.commission_price = float(h_l1.commission_price)
        except Exception:
            pass
        # 品牌部分主要维护自平台定义的品牌，不对抓取的品牌进行入库
        self.brand_name_sp = h_l1.brand_name
        # todo self.brand_id_sp
        self.deposit_type = h_l1.deposit_type
        self.status = h_l1.status
        self.src_type = h_l1.src_type
        self.user_name = h_l1.user_name
        self.user_phone = h_l1.user_phone
        self.user_type = h_l1.user_type
        self.pay_type = h_l1.pay_type
        self.update_device(h_l1.device_tag, h_l1.service_tag, device_list)
        self.decoration_type = h_l1.decoration_type
        # self.bus_id self.bus_desc self.metro_id self.metro_desc 有reuest poi填写
        self.tag = ''
        self.create_time = h_l1.create_time
        self.update_time = h_l1.update_time
        self.scrapy_time = h_l1.scrapy_time
        self.hashStr = h_l1.hashStr
        # self.hash_img 由图片上传任务填写
        # self.version 根据版本更新填写
        # self.house_oid 由聚类任务填写
        # self.tile_x self.tile_y 由经纬度计算方法填写
        return self.check_valid() and self.price > 0

    # 判断数据是否可用
    def check_valid(self):
        return isinstance(self.house_uid, str) and len(self.house_uid) > 0 and self.city_id != 0 and \
               self.district_id != 0

    def check_locus(self, h_l2):
        if h_l2 is None:
            self.flag_locus = 0
        elif h_l2.price == 0 or h_l2.status == 0:
            self.flag_locus = 0
        elif self.price == 0 or self.status == 0:
            self.flag_locus = 0
        elif h_l2.price != self.price or h_l2.status != self.status:
            self.flag_locus = 1

    # 计算房源的唯一ID
    def hash_house_uid(self):
        self.house_uid = hash.sha1(self.third_house_id + 'sh' + str(self.city_id) + 'gyj' + str(self.district_id))

    # 计算特征hash
    def hash_feture_cal(self):
        self.hash_feture = hash.sha1(str(self.city_id) + '/'
                                     + str(self.district_id) + '/'
                                     + self.community_name + '/'
                                     + str(self.room) + '/'
                                     + str(self.living) + '/'
                                     + str(self.washing) + '/'
                                     + str(self.cook) + '/'
                                     + str(self.balcony) + '/'
                                     + str(int(self.building_area)) + '/'
                                     + str(tool_l3.convrt_direction(self.direction)))
        return self.hash_feture

    def hash_feture_self_cal(self):
        self.hash_feture_self = hash.sha1(self.house_uid)
        return self.hash_feture_self

    # 计算等级hash
    def level_feture_cal(self):
        self.level_feture = tool_l3.convert_device_level(self.device_id, self.rent_period)
        return self.level_feture

    def level_feture_self_cal(self):
        self.level_feture_self = 'A'
        return self.level_feture_self

    # 将所在楼层转换成标准化格式：
    def convert_onfloor(self):
        return tool_l3.convert_onfloor(self.on_floor, self.total_floor)

    # 更新版本号
    def update_version(self):
        self.version += 1
        self.update_time = log.now()

    def update_device(self, device_tag, service_tag, device_list):
        # 添加室内室外设备情况
        if isinstance(device_list, list):
            for d in device_list:
                if d.device_type == 1 and isinstance(device_tag, str):
                    did = 0
                    if re.search(d.device_name, device_tag, 0):
                        did = d.id
                    if did == 0 and d.other_name:
                        other_names = d.other_name.split(',')
                        for od in other_names:
                            if re.search(od, device_tag, 0):
                                did = d.id
                                break
                    if did != 0:
                        if len(self.device_id) > 0:
                            self.device_id += ','
                        self.device_id += str(did)
                elif d.device_type == 2 and isinstance(service_tag, str):
                    did = 0
                    if re.search(d.device_name, service_tag, 0):
                        did = d.id
                    if did == 0 and d.other_name:
                        other_names = d.other_name.split(',')
                        for od in other_names:
                            if re.search(od, device_tag, 0):
                                did = d.id
                                break
                    if did != 0:
                        if len(self.service_id) > 0:
                            self.service_id += ','
                        self.service_id += str(did)

    # 更新商圈信息
    def update_business(self):
        if self.business_id_v2 != 0:
            log.logd1('fun request_poi: business already have [%s][%d]' % (self.house_uid, self.business_id_v2))
            return True
        tile = db_l2.query_tile_l2(self.city_id, self.hash_tile)
        if isinstance(tile, TileL2):
            if tile.valid():
                self.business_id_v2 = tile.business_id
            else:
                # todo 确认格式化写法正确
                self.business_id_v2 = int("{0:0<6}".format(self.city_id))
            return True
        return False

    # 更新小区信息
    def update_community(self, community_map):
        # 添加小区信息
        if self.community_name is None or len(self.community_name) == 0:
            return False
        c = CommunityL2()
        c.fill_with_l2(self)
        self.community_id_v2 = c.community_uid
        if c.community_uid not in community_map.keys():
            # 如果L2库中没有该小区，则入库
            c = db_l2.insert_community_l2(c)
            if c is not None:
                community_map[c.community_uid] = c
            else:
                return False
        return True

    # 检索填充经纬度
    def query_location(self, city_name, dist, business_name):
        if self.latitude <= 0 or self.longtitude <= 0:
            req_addr = ''
            if dist is not None:
                if dist.is_real():
                    req_addr += city_name
                    req_addr += dist.name
                elif self.address:
                    # 针对特殊的行政区（如上海周边），将城市和行政区部分从地址检索中剔除以保证精确度
                    if dist.name in self.address:
                        self.address = self.address.replace(dist.name, '')
                    if dist.shortname in self.address:
                        self.address = self.address.replace(dist.shortname, '')
            req_addr += business_name
            req_addr += self.address
            req_addr += self.community_name
            location = lbs.request_baidu_location(req_addr)
            if location is not None:
                self.latitude = location.lat
                self.longtitude = location.lng
        else:
            log.logd1('fun query_location: location already have')

    def query_tile(self):
        if self.latitude > 0 and self.longtitude > 0:
            # 计算瓦片坐标
            self.tile_x, self.tile_y, self.hash_tile = tool_l2.make_tile_location(self.city_id, self.latitude,
                                                                                  self.longtitude)
        log.logd1('house [%s] tile: %d,%d,%s' % (self.house_uid, self.tile_x, self.tile_y, self.hash_tile))

    # 检索填充地铁公交线路信息
    def request_poi(self, trans_site, trans_line):
        if self.bus_id is not None and len(self.bus_id) > 0 \
                and self.bus_desc is not None and len(self.bus_desc) > 0 \
                and self.metro_id is not None and len(self.metro_id) > 0 \
                and self.metro_desc is not None and len(self.metro_desc) > 0:
            log.logd1('fun request_poi: poi already have')
            return True
        if self.latitude > 0 and self.longtitude > 0:
            poi_list = []
            for idx in range(0, 1):
                poi = lbs.request_baidu_poi(self.latitude, self.longtitude, idx)
                for p in poi.results:
                    if lbs.is_transport_addr(p, self.city_id):
                        poi_list.append(p)
                if len(poi.results) < 20:
                    break
            log.logd1('request pos found [%d] result' % len(poi_list))
            if len(poi_list) > 0:
                self.bus_id = ''
                self.bus_desc = ''
                self.metro_id = ''
                self.metro_desc = ''
                for p in poi_list:
                    if p is None:
                        continue
                    # 站点ID
                    tid = 0
                    if p.name in trans_site:
                        tid = trans_site[p.name].id
                    if tid == 0:
                        # 没有入过库的站点，先将其所属的所有线路入库
                        site_lines = ''
                        tlines = p.address.split(';')
                        for lname in tlines:
                            # 追加线路ID
                            lid = 0
                            if lname in trans_line:
                                lid = trans_line[lname].id
                            if lid == 0:
                                # 对线路信息进行入库
                                tline = TransportL2()
                                tline.trans_name = lname
                                if p.trans_type == 1:
                                    tline.trans_type = 3
                                else:
                                    tline.trans_type = 4
                                tline.city_id = self.city_id
                                tline.district_id = self.district_id
                                tline = db_l2.insert_transport_l2(tline)
                                if tline is None:
                                    return False
                                trans_line[tline.trans_name] = tline
                                lid = tline.id
                            if len(site_lines) > 0:
                                site_lines += ','
                            site_lines += str(lid)
                        if len(site_lines) == 0:
                            return False
                        # 再对站点本身进行入库
                        t = TransportL2()
                        t.fill_with_poi(p)
                        t.parent_id = site_lines
                        t.city_id = self.city_id
                        t.district_id = self.district_id
                        t = db_l2.insert_transport_l2(t)
                        if t is None:
                            return False
                        trans_site[t.trans_name] = t
                        tid = t.id
                    if p.trans_type == 1:
                        # 地铁站
                        if len(self.metro_id) > 0:
                            self.metro_id += ','
                        self.metro_id += str(tid)
                        if len(self.metro_desc) > 0:
                            self.metro_desc += ','
                        self.metro_desc += str(tid) + '|' + p.name + '|' + str(p.distance)
                    if p.trans_type == 2:
                        # 公交站
                        if len(self.bus_id) > 0:
                            self.bus_id += ','
                        self.bus_id += str(tid)
                        if len(self.bus_desc) > 0:
                            self.bus_desc += ','
                        self.bus_desc += str(tid) + '|' + p.name + '|' + str(p.distance)
            return True

    def fill_with_admin(self, h_yo, city_id, dist_id, brands, devices):
        if h_yo.src_type == 4:
            self.src_type = 6668
            self.third_house_id = '6668_%d' % h_yo.id
        elif h_yo.src_type == 5:
            self.src_type = 6667
            self.third_house_id = '6667_%d' % h_yo.id
        else:
            self.src_type = 6666
            self.third_house_id = '6666_%d' % h_yo.id
        self.city_id = city_id
        self.district_id = dist_id
        # todo self.business_id_v2
        self.house_name = h_yo.house_name
        self.house_url = ''
        self.house_type = str(h_yo.house_type)
        self.community_name = h_yo.community_name
        self.address = h_yo.address
        self.house_desc = h_yo.house_info
        self.on_floor = str(h_yo.on_floor)
        self.total_floor = str(h_yo.total_floor)
        self.building = h_yo.building
        self.room_number = h_yo.room_number
        self.building_area = h_yo.building_area
        self.room = h_yo.bed_room
        self.living = h_yo.living_room
        self.washing = h_yo.washing_room
        self.cook = 0
        self.balcony = 0
        self.latitude = h_yo.latitude
        self.longtitude = h_yo.longitude
        self.rent_mode = h_yo.rent_mode
        if h_yo.rent_type == 3:
            self.rent_period = 3
        else:
            self.rent_period = 1
        # 朝向 1 东 2南 3 西 4 北 5 东南 6 东北 7 西南 8 西北
        if h_yo.direction == 1:
            self.direction = '1000'
        elif h_yo.direction == 2:
            self.direction = '0010'
        elif h_yo.direction == 3:
            self.direction = '0100'
        elif h_yo.direction == 4:
            self.direction = '0001'
        elif h_yo.direction == 5:
            self.direction = '1010'
        elif h_yo.direction == 6:
            self.direction = '1001'
        elif h_yo.direction == 7:
            self.direction = '0110'
        elif h_yo.direction == 8:
            self.direction = '0101'
        if h_yo.rent_type == 3:
            # 按天
            self.price_detail = str(h_yo.price / 30) + '|0|0|0|0'
            self.pay_type = 5
        elif h_yo.rent_type == 2:
            # 按年
            self.price_detail = '0|0|0|0|' + str(h_yo.price * 12)
            self.pay_type = 3
        else:
            # 按月
            self.price_detail = '0|' + str(h_yo.price) + '|0|0|0'
            self.pay_type = 1
        self.price = tool_l2.convert_price(self.price_detail, h_yo.price)[0]
        self.service_fee = '0|0|0|0|0'
        try:
            self.commission_price = float(h_yo.full_commission)
        except Exception:
            pass
        if h_yo.partner_id != 0 and h_yo.partner_id in brands.keys():
            self.brand_id = brands[h_yo.partner_id].id
            self.brand_name = brands[h_yo.partner_id].brand_name
        # 1 付一押一 2 付一押二 3 付二押一 4 付二押二 5 付三押一 6 付三押二 7 半年付 8 年付
        if h_yo.rent_pay_type == 1 or h_yo.rent_pay_type == 3 or h_yo.rent_pay_type == 5:
            self.deposit_type = 1
        elif h_yo.rent_pay_type == 2 or h_yo.rent_pay_type == 4 or h_yo.rent_pay_type == 6:
            self.deposit_type = 2
        if h_yo.status == 2 or h_yo.status == 3:
            self.status = 2
        else:
            self.status = 1
        self.user_name = h_yo.contact_name
        self.user_phone = h_yo.contact_phone
        self.user_type = 1
        for dv in devices:
            if dv.device_type == 1:
                if len(self.device_id) > 0:
                    self.device_id += ','
                self.device_id += str(dv.id)
            elif dv.device_type == 2:
                if len(self.service_id) > 0:
                    self.service_id += ','
                self.service_id += str(dv.id)
        self.tag = h_yo.tags
        self.create_time = h_yo.create_time
        self.update_time = h_yo.update_time
        self.hashStr = h_yo.hash_str
        if h_yo.decorate_level == 1:
            # 毛坯
            self.decoration_type = 4
        elif h_yo.decorate_level == 2:
            # 普通
            self.decoration_type = 3
        elif h_yo.decorate_level == 3:
            # 精装
            self.decoration_type = 1
        elif h_yo.decorate_level == 4:
            # 豪华
            self.decoration_type = 1
        if h_yo.is_landlord == 1:
            # 租客
            self.tenant = h_yo.user_id
        else:
            # 房东等
            self.landlord = h_yo.user_id
        self.hashStr = h_yo.hash_str

    def to_locus(self):
        locus = Locus()
        locus.city_id = self.city_id
        locus.house_uid = self.house_uid
        locus.price = self.price
        locus.status = self.status
        if locus.status == 2:
            locus.timestamp = tool_l2.mk_unixtime(self.scrapy_time)
        elif locus.status == 1:
            locus.timestamp = tool_l2.mk_unixtime(self.update_time)
        return locus

    def unusual_price(self):
        return self.price > 500000 or self.price <= 0

    def unusual_room(self):
        return self.room <= 0


# L1级库房源图片信息
class HousePicL1:
    id = 0
    house_id = ''
    pic_url = ''
    failure_num = 0
    pic_url_key = ''
    is_cover = 2

    def __init__(self, data):
        self.id = int(data[0])
        self.house_id = data[1]
        self.pic_url = data[2]
        try:
            self.failure_num = int(data[3])
        except Exception:
            self.failure_num = 0
        self.pic_url_key = hash.md5(str(self.pic_url))


# L2级库房源图片信息
class HousePicL2:
    id = 0
    house_uid = ''
    pic_url = ''
    pic_path = ''
    src_type = 0
    is_qiniu = 0
    is_cover = 0
    is_delete = 0
    create_time = ''
    update_time = ''
    pic_url_key = ''
    # 是否还存在
    check_exist = False

    def __init__(self):
        pass

    def fill_with_db(self, data):
        self.id = int(data[0])
        self.house_uid = data[1]
        self.pic_url = data[2]
        self.pic_path = data[3]
        self.src_type = int(data[4])
        self.is_qiniu = int(data[5])
        self.is_cover = int(data[6])
        self.is_delete = int(data[7])
        self.create_time = int(data[8])
        self.update_time = int(data[9])
        self.pic_url_key = hash.md5(self.pic_url)


# L3级库房源基本信息
class HouseIntervL3:
    house_oid = 0
    hash_feture = ''
    level_feture = ''
    city_id = 0
    district_id = 0
    business_id_v2 = 0
    check_status = 0  # 1-待审核；2-审核通过；3-审核拒绝
    status = 0  # 1-已租；2-可租
    upon_status = 0  # 1-上架；2-下架
    create_time = 0
    update_time = 0
    user_phone = ''
    relative_id_main = 0
    house_number = 0
    src_type_number = 0
    latitude = 0.0
    longtitude = 0.0
    price_ave = 0.0
    metro_id = 0
    community_id_v2 = ''
    room = 0
    # 非数据库字段
    hash_img = ''

    def __init__(self):
        pass

    def fill_with_db(self, data):
        self.house_oid = int(data[0])
        try:
            self.city_id = int(data[1])
        except Exception:
            pass
        try:
            self.district_id = int(data[2])
        except Exception:
            pass
        try:
            self.business_id_v2 = int(data[3])
        except Exception:
            pass
        try:
            self.check_status = int(data[4])
        except Exception:
            pass
        try:
            self.status = int(data[5])
        except Exception:
            pass
        try:
            self.upon_status = int(data[6])
        except Exception:
            pass
        try:
            self.create_time = int(data[7])
        except Exception:
            pass
        try:
            self.update_time = int(data[8])
        except Exception:
            pass
        self.user_phone = data[9]
        try:
            self.relative_id_main = int(data[10])
        except Exception:
            pass
        try:
            self.house_number = int(data[11])
        except Exception:
            pass
        try:
            self.src_type_number = int(data[12])
        except Exception:
            pass
        try:
            self.latitude = float(data[13])
        except Exception:
            pass
        try:
            self.longtitude = float(data[14])
        except Exception:
            pass
        try:
            self.price_ave = float(data[15])
        except Exception:
            pass
        try:
            self.metro_id = int(data[16])
        except Exception:
            pass
        self.community_id_v2 = data[17]

    # 判断是否需要更新interv数据
    def check_update(self, h_l2):
        if self.relative_id_main == 0:
            # 关联主源为0则必须更新
            return True
        if h_l2 is not None:
            # 传入的单房源信息不为空时，以单房源为基准去判断调整
            if self.house_number != 1 or self.src_type_number != 1:
                return True
            if self.price_ave != h_l2.price \
                    or self.status != h_l2.status \
                    or self.community_id_v2 != h_l2.community_id_v2 \
                    or self.user_phone != h_l2.user_phone \
                    or self.metro_id != tool_l3.find_nearest_metro(h_l2.metro_desc):
                return True
        return False

    # 以单房源数据更新interv
    def update_interv_with_self_l2(self, h_l2):
        self.house_number = 1
        self.src_type_number = 1
        self.price_ave = h_l2.price
        self.status = h_l2.status
        self.metro_id = tool_l3.find_nearest_metro(h_l2.metro_desc)
        self.community_id_v2 = h_l2.community_id_v2
        self.user_phone = h_l2.user_phone

    # 更新上下架状态
    def update_upon_status(self):
        if self.status == 2 and self.price_ave >= 500 and len(self.hash_img) > 0 and len(self.user_phone) > 0:
            self.upon_status = 1
        else:
            self.upon_status = 2
        log.logd2('func update_upon_status: [%d][%d]' % (self.house_oid, self.upon_status))


# L3级库房源聚类关系
class HouseRelativeL3:
    relative_id = 0
    house_oid = 0
    house_uid = ''
    src_type = 0
    # 1-非主房源；2-主房源
    is_main = 0
    sort = 0
    # 1-未审核；2-已审核通过；3-审核不通过
    status = 0

    def __init__(self):
        pass

    def fill_with_db(self, data):
        self.relative_id = int(data[0])
        self.house_oid = int(data[1])
        self.src_type = int(data[2])
        self.status = int(data[3])
