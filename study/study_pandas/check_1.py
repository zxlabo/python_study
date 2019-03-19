from sqlalchemy import create_engine
import pandas as pd

sql_conn = "mysql+pymysql://online_pontus_r:iYo8900@p@rm-uf65b1di3b76cbz0e.mysql.rds.aliyuncs.com:3306/gyj_pontus"
# sql_conn = "mysql+pymysql://root:899036c045@120.26.130.180:3306/gyj_pontus"

engine = create_engine(sql_conn)


def query_l3(l3_metro_id):
    sql_query_l3 = "select house_oid from l3_house_interv WHERE metro_id =%d" % l3_metro_id
    l3_result = pd.read_sql_query(sql_query_l3, con=engine)
    print(sql_query_l3)
    if len(l3_result) > 0:
        print("error")


def query_l2_metro(l2_metro_id):
    sql_query_l3 = "select * from l2_house_sp_934 WHERE FIND_IN_SET(%d,metro_id)" % l2_metro_id
    l2_metro_result = pd.read_sql_query(sql_query_l3, con=engine)
    print(sql_query_l3)
    if len(l2_metro_result) > 0:
        print("error")


def query_l2_bus(bus_id):
    sql_query_l3 = "select * from l2_house_sp_934 WHERE FIND_IN_SET(%d,bus_id)" % bus_id
    l2_bus_result = pd.read_sql_query(sql_query_l3, con=engine)
    print(sql_query_l3)
    if len(l2_bus_result) > 0:
        print("error")


def query_l2_parent(parent_id):
    sql_query_l3 = "select * from l2_transport WHERE FIND_IN_SET(%d,parent_id)" % parent_id
    l2_parent_result = pd.read_sql_query(sql_query_l3, con=engine)
    print(sql_query_l3)
    if len(l2_parent_result) > 0:
        print("error")


def check():
    sql_list = []
    sql_query1 = "SELECT id FROM `l2_transport` WHERE `trans_name` ='七堡' and `district_id` =937 and `trans_type` =1 and `level` =8"
    sql_query2 = "SELECT id FROM `l2_transport` WHERE `trans_name` ='甬江路' and `district_id` =935 and `trans_type` =1 and `level` =8"
    sql_query3 = "SELECT id FROM `l2_transport` WHERE `trans_name` ='近江' and `district_id` =935 and `trans_type` =1 and `level` =8"
    sql_list.append(sql_query1)
    sql_list.append(sql_query2)
    sql_list.append(sql_query3)
    for sql_query in sql_list:
        trans_list = pd.read_sql_query(sql_query, con=engine).values
        for trans_item in trans_list:
            trans_id = trans_item[0]
            query_l3(trans_id)
            query_l2_metro(trans_id)
            # if trans_type == 1:
            #     query_l3(trans_id)
            #     query_l2_metro(trans_id)
            # elif trans_type == 2:
            #     query_l2_bus(trans_id)
            # else:
            #     query_l2_parent(trans_id)


check()
