from sqlalchemy import create_engine
import pandas as pd

# sql_conn = "mysql+pymysql://online_pontus_r:iYo8900@p@rm-uf65b1di3b76cbz0e.mysql.rds.aliyuncs.com:3306/gyj_pontus"
sql_conn = "mysql+pymysql://root:899036c045@120.26.130.180:3306/gyj_pontus"

engine = create_engine(sql_conn)


def query_repeat_trans(trans_type):
    sql_query = "SELECT trans_name,district_id FROM ( SELECT *, CONCAT( trans_name, district_id ) " \
                "AS nameAndCode FROM l2_transport WHERE city_id=934 and `level`=8 and trans_type=%d limit 10) t  " \
                "WHERE t.nameAndCode IN " \
                "( SELECT nameAndCode FROM ( SELECT CONCAT( trans_name, district_id ) AS nameAndCode FROM " \
                "l2_transport ) tt GROUP BY nameAndCode HAVING count( nameAndCode ) > 1 )" % trans_type
    print(sql_query)
    id_list = pd.read_sql_query(sql_query, con=engine).values
    print(len(id_list))
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


for idx_type in range(1, 3):
    query_repeat_trans(idx_type)
