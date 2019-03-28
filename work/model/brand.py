# coding=utf-8

import time


class BrandL2:
    id = 0
    brand_name = ''
    brand_type = 0
    company_name = ''
    brand_background = ''
    brand_slogan = ''
    brand_logo = ''
    brand_desc = ''
    address = ''
    status = 0
    contact_name = ''
    contact_mobile = ''
    reserve_mobile = ''
    sort = 0
    is_delete = 0
    create_time = 0
    update_time = 0
    in_hot_citys = ''
    id_relative_partner = 0
    hash_str = ''
    ka_code = ''
    reason = ''

    def __init__(self):
        pass

    def fill_all(self, data):
        self.id = int(data[0])
        self.brand_name = data[1]
        try:
            self.brand_type = int(data[2])
        except Exception:
            pass
        self.company_name = data[3]
        self.brand_background = data[4]
        self.brand_slogan = data[5]
        self.brand_logo = data[6]
        self.brand_desc = data[7]
        self.address = data[8]
        try:
            self.status = int(data[9])
        except Exception:
            pass
        self.contact_name = data[10]
        self.contact_mobile = data[11]
        self.reserve_mobile = data[12]
        try:
            self.sort = int(data[13])
        except Exception:
            pass
        try:
            self.is_delete = int(data[14])
        except Exception:
            pass
        self.create_time = data[15]
        self.update_time = data[16]
        self.in_hot_citys = data[17]
        try:
            self.id_relative_partner = int(data[18])
        except Exception:
            pass
        self.hash_str = data[19]

    def fill_hash(self, data):
        self.id = int(data[0])
        try:
            self.id_relative_partner = int(data[1])
        except Exception:
            pass
        self.hash_str = data[2]
        self.brand_name = data[3]

    def fill_with_admin(self, admin_brand):
        self.brand_name = admin_brand.brand_name
        self.brand_type = admin_brand.partner_type
        self.company_name = admin_brand.partner_name
        self.brand_slogan = ''
        self.brand_desc = admin_brand.brand_desc
        self.address = admin_brand.address
        if admin_brand.status == 1:
            self.status = 2
        elif admin_brand.status == 2:
            self.status = 3
        elif admin_brand.status == 3:
            self.status = 1
        self.contact_name = admin_brand.contact_name
        self.contact_mobile = admin_brand.contact_mobile
        self.reserve_mobile = admin_brand.contact_phone
        self.sort = 0
        self.is_delete = 0
        try:
            self.create_time = time.mktime(time.strptime(str(admin_brand.create_time), "%Y-%m-%d %H:%M:%S"))
        except Exception:
            pass
        try:
            self.update_time = time.mktime(time.strptime(str(admin_brand.update_time), "%Y-%m-%d %H:%M:%S"))
        except Exception:
            pass
        self.in_hot_citys = ''
        self.id_relative_partner = admin_brand.id
        self.hash_str = admin_brand.hash_str
        self.ka_code = admin_brand.ka_code
        self.reason = admin_brand.reason

    def valid(self):
        return self.brand_name is not None and len(self.brand_name) > 0 \
               and self.hash_str is not None and len(self.hash_str) > 0



