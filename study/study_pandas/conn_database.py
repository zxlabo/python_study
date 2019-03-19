# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
import pandas as pd
import os
import sys

p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.extend([p])
from common import config

configs = config.load_config(['db_host_pontus', 'db_user_pontus', 'db_pwd_pontus'])
db_host = configs['db_host_pontus']
db_user = configs['db_user_pontus']
db_pwd = configs['db_pwd_pontus']
sql_conn = 'mysql+pymysql://' + db_user + ':' + db_pwd + '@' + db_host + ':3306/gyj_pontus'
print(sql_conn)
engine = create_engine(sql_conn)


def query_repeat_trans(trans_type):
    sql_query = "SELECT trans_name,district_id FROM ( SELECT *, CONCAT( trans_name, district_id ) " \
                "AS nameAndCode FROM l2_transport WHERE `level`=8 and trans_type=%d ) t  WHERE t.nameAndCode IN " \
                "( SELECT nameAndCode FROM ( SELECT CONCAT( trans_name, district_id ) AS nameAndCode FROM " \
                "l2_transport ) tt GROUP BY nameAndCode HAVING count( nameAndCode ) > 1 )" % trans_type
    id_list = pd.read_sql_query(sql_query, con=engine).values
    check(trans_type, id_list)


def query_l3(l3_metro_id):
    sql_query_l3 = "select house_oid from l3_house_interv WHERE metro_id =%d" % l3_metro_id
    l3_result = pd.read_sql_query(sql_query_l3, con=engine)
    if len(l3_result) > 0:
        print(sql_query_l3)


def query_l2_metro(l2_metro_id):
    sql_query_l3 = "select * from l2_house_sp_934 WHERE FIND_IN_SET(%d,metro_id)" % l2_metro_id
    l2_metro_result = pd.read_sql_query(sql_query_l3, con=engine)
    if len(l2_metro_result) > 0:
        print(sql_query_l3)


def query_l2_bus(bus_id):
    sql_query_l3 = "select * from l2_house_sp_934 WHERE FIND_IN_SET(%d,bus_id)" % bus_id
    l2_bus_result = pd.read_sql_query(sql_query_l3, con=engine)
    if len(l2_bus_result) > 0:
        print(sql_query_l3)


def query_l2_parent(parent_id):
    sql_query_l3 = "select * from l2_transport WHERE FIND_IN_SET(%d,parent_id)" % parent_id
    l2_parent_result = pd.read_sql_query(sql_query_l3, con=engine)
    if len(l2_parent_result) > 0:
        print(sql_query_l3)


def check(trans_type, id_list):
    i = 0
    for item in id_list:
        sql_query_trans = "select id from l2_transport WHERE level=8 and trans_type=%d and trans_name='%s'" \
                          " AND district_id=%d" % (trans_type, item[0], item[1])
        trans_list = pd.read_sql_query(sql_query_trans, con=engine).values
        for trans_item in trans_list:
            trans_id = trans_item[0]
            if trans_type == 1:
                query_l3(trans_id)
                query_l2_metro(trans_id)
            elif trans_type == 2:
                query_l2_bus(trans_id)
            else:
                query_l2_parent(trans_id)
        i += 1
        if i > 10:
            break


for idx_type in range(1, 5):
    query_repeat_trans(idx_type)
