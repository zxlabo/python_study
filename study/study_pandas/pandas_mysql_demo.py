# -*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine

from pandas import DataFrame
from pandasql import sqldf, load_meat, load_births

sql_conn = "mysql+pymysql://root:899036c045@120.26.130.180:3306/gyj_pontus"
engine = create_engine(sql_conn)


def query_repeat_trans(trans_type):
    global table_name
    sql_query = "SELECT trans_name,district_id FROM ( SELECT *, CONCAT( trans_name, district_id ) " \
                "AS nameAndCode FROM l2_transport WHERE `level`=8 and trans_type=%d ) t  WHERE t.nameAndCode IN " \
                "( SELECT nameAndCode FROM ( SELECT CONCAT( trans_name, district_id ) AS nameAndCode FROM " \
                "l2_transport ) tt GROUP BY nameAndCode HAVING count( nameAndCode ) > 1 )" % trans_type
    table_name = pd.read_sql_query(sql_query, con=engine)
    pysqldf = lambda sql: sqldf(sql, globals())
    sql = "select * from table_name where trans_name ='中河北路'"
    print(pysqldf(sql))


def query_l2_metro(l2_metro_id):
    sql_query_l3 = "select * from l2_house_sp_934 WHERE FIND_IN_SET(%d,metro_id)" % l2_metro_id
    l2_metro_result = pd.read_sql_query(sql_query_l3, con=engine)
    if len(l2_metro_result) > 0:
        print(sql_query_l3)


def query_l2_house():
    global l2_house_sp
    sql_query_l3 = "select house_uid,metro_id from l2_house_sp_934 "
    l2_house_sp = pd.read_sql_query(sql_query_l3, con=engine)
    pysqldf = lambda sql: sqldf(sql, globals())
    sql = "select * from l2_house_sp WHERE FIND_IN_SET(25783,metro_id)"
    print(pysqldf(sql))
    # if len(l2_house_sp) > 0:
    #     print(l2_house_sp)
    #     print(sql_query_l3)


# query_repeat_trans(1)
query_l2_house()
