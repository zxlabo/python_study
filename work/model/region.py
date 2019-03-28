# coding=utf-8

from model.house import HouseL2
from common import log


# 房源的区域性数据
class RegionSummary:
    city_id = 0
    district_id = 0
    business_id = 0
    is_self = False
    timestamp = 0
    # 区域内的房源数、价格、卧室数等
    house_total = 0
    price_total = 0
    room_total = 0
    house_online = 0
    price_online = 0
    room_online = 0
    house_deal = 0
    price_deal = 0
    room_deal = 0
    # 价格分段
    region_price_total = None
    region_price_online = None
    # 户型
    region_layout_total = None
    region_layout_online = None
    # 异常数据
    unusual_price_house = 0
    unusual_room_house = 0

    def __init__(self, city_id, dist_id, business_id):
        self.city_id = city_id
        self.district_id = dist_id
        self.business_id = business_id
        self.region_price_total = RegionPrice()
        self.region_price_online = RegionPrice()
        self.region_layout_total = RegionLayout()
        self.region_layout_online = RegionLayout()

    def valid(self):
        return self.city_id != 0 and self.district_id != 0

    def append_house(self, h_l2):
        if not isinstance(h_l2, HouseL2):
            log.error('func append_house input h_l2 invalid')
        self.house_total += 1
        self.price_total += h_l2.price
        self.room_total += h_l2.room
        self.region_price_total.append_house(h_l2)
        self.region_layout_total.append_house(h_l2)
        if h_l2.status == 2:
            self.house_online += 1
            self.price_online += h_l2.price
            self.room_online += h_l2.room
            self.region_price_online.append_house(h_l2)
            self.region_layout_online.append_house(h_l2)
        if h_l2.flag_locus == 1 and h_l2.status == 1:
            self.house_deal += 1
            self.price_deal += h_l2.price
            self.room_deal += h_l2.room

    def append_db(self, data):
        self.house_total += int(data[2])
        self.price_total += float(data[3])
        self.room_total += int(data[4])
        self.region_price_total.append_db(data)
        self.region_layout_total.append_db(data)
        if int(data[1]) == 2:
            self.house_online += int(data[2])
            self.price_online += float(data[3])
            self.room_online += int(data[4])
            self.region_price_online.append_db(data)
            self.region_layout_online.append_db(data)

    def append_unusual(self, h_l2):
        if not isinstance(h_l2, HouseL2):
            log.error('func append_unusual input h_l2 invalid')
        if h_l2.unusual_price():
            log.logd6('l2 house [%s] unusual price [%f]' % (h_l2.house_uid, h_l2.price))
            self.unusual_price_house += 1
        if h_l2.unusual_room():
            log.logd6('l2 house [%s] unusual room [%d]' % (h_l2.house_uid, h_l2.room))
            self.unusual_room_house += 1

    def have_unusual(self):
        return self.unusual_room_house > 0 or self.unusual_price_house > 0


class RegionPrice:
    p1000 = 0
    p1500 = 0
    p2000 = 0
    p3000 = 0
    p4000 = 0
    p5000 = 0
    p6000 = 0
    p7000 = 0
    p8000 = 0
    p9000 = 0
    p10000 = 0
    p15000 = 0
    p20000 = 0
    p25000 = 0
    pmax = 0

    def __init__(self):
        pass

    def append_house(self, h_l2):
        if isinstance(h_l2, HouseL2):
            if h_l2.price <= 1000:
                self.p1000 += 1
            elif h_l2.price <= 1500:
                self.p1500 += 1
            elif h_l2.price <= 2000:
                self.p2000 += 1
            elif h_l2.price <= 3000:
                self.p3000 += 1
            elif h_l2.price <= 4000:
                self.p4000 += 1
            elif h_l2.price <= 5000:
                self.p5000 += 1
            elif h_l2.price <= 6000:
                self.p6000 += 1
            elif h_l2.price <= 7000:
                self.p7000 += 1
            elif h_l2.price <= 8000:
                self.p8000 += 1
            elif h_l2.price <= 9000:
                self.p9000 += 1
            elif h_l2.price <= 10000:
                self.p10000 += 1
            elif h_l2.price <= 15000:
                self.p15000 += 1
            elif h_l2.price <= 20000:
                self.p20000 += 1
            elif h_l2.price <= 25000:
                self.p25000 += 1
            else:
                self.pmax += 1

    def append_db(self, data):
        self.p1000 += int(data[12])
        self.p1500 += int(data[13])
        self.p2000 += int(data[14])
        self.p3000 += int(data[15])
        self.p4000 += int(data[16])
        self.p5000 += int(data[17])
        self.p6000 += int(data[18])
        self.p7000 += int(data[19])
        self.p8000 += int(data[20])
        self.p9000 += int(data[21])
        self.p10000 += int(data[22])
        self.p15000 += int(data[23])
        self.p20000 += int(data[24])
        self.p25000 += int(data[25])
        self.pmax += int(data[26])


class RegionLayout:
    room0 = 0
    room1 = 0
    room2 = 0
    room3 = 0
    room4 = 0
    room5 = 0
    room6_plus = 0

    def __init__(self):
        pass

    def append_house(self, h_l2):
        if isinstance(h_l2, HouseL2):
            if h_l2.room < 1:
                self.room0 += 1
            elif h_l2.room == 1:
                self.room1 += 1
            elif h_l2.room == 2:
                self.room2 += 1
            elif h_l2.room == 3:
                self.room3 += 1
            elif h_l2.room == 4:
                self.room4 += 1
            elif h_l2.room == 5:
                self.room5 += 1
            elif h_l2.room > 5:
                self.room6_plus += 1

    def append_db(self, data):
        self.room0 += int(data[5])
        self.room1 += int(data[6])
        self.room2 += int(data[7])
        self.room3 += int(data[8])
        self.room4 += int(data[9])
        self.room5 += int(data[10])
        self.room6_plus += int(data[11])
