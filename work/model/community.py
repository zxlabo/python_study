# coding=utf-8

import time

from common import hash


class CommunityL2:
    community_uid = ''
    community_name = ''
    city_id = 0
    district_id = 0
    business_id_v2 = 0
    address = ''
    latitude = ''
    longtitude = ''
    create_time = ''
    update_time = ''

    def hash_community_uid(self):
        self.community_uid = hash.sha1(
            'com' + str(self.city_id) + 'gyj' + str(self.district_id) + self.community_name)

    def fill_with_l2(self, h_l2):
        self.community_name = h_l2.community_name
        self.city_id = h_l2.city_id
        self.district_id = h_l2.district_id
        self.business_id_v2 = h_l2.business_id_v2
        self.address = h_l2.address
        self.latitude = h_l2.latitude
        self.longtitude = h_l2.longtitude
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.create_time = t
        self.update_time = t
        self.hash_community_uid()

    def fill_with_db(self, data):
        self.community_uid = str(data[0])
        self.community_name = str(data[1])
        self.city_id = int(data[2])
        self.district_id = int(data[3])
        self.business_id_v2 = int(data[4])
        self.address = str(data[5])
        self.latitude = str(data[6])
        self.longtitude = str(data[7])
        self.create_time = str(data[8])
        self.update_time = str(data[9])
