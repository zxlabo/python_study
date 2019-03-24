from sqlalchemy import create_engine
import pandas as pd

sql_conn = "mysql+pymysql://online_pontus_r:iYo8900@p@rm-uf65b1di3b76cbz0e.mysql.rds.aliyuncs.com:3306/gyj_pontus"
# sql_conn = "mysql+pymysql://root:899036c045@120.26.130.180:3306/gyj_pontus"

engine = create_engine(sql_conn)


def query_l2_parent(parent_id):
    sql_query_l3 = "select * from l2_transport WHERE FIND_IN_SET(%d,parent_id)" % parent_id
    l2_parent_result = pd.read_sql_query(sql_query_l3, con=engine)
    print(sql_query_l3)
    if len(l2_parent_result) > 0:
        print("error")


def check():
    sql_list = []
    sql_query1 = "select * FROM `l2_transport` WHERE `trans_name` ='1001路' AND `district_id` =2373  AND `trans_type` =4 and `level` =8"
    sql_query2 = "select * FROM `l2_transport` WHERE `trans_name` ='1091路' AND `district_id` =2372  AND `trans_type` =4 and `level` =8"
    sql_query3 = "select * FROM `l2_transport` WHERE `trans_name` ='10路' AND `district_id` =2372  AND `trans_type` =4 and `level` =8"
    sql_query4 = "select * FROM `l2_transport` WHERE `trans_name` ='165路' AND `district_id` =2370  AND `trans_type` =4 and `level` =8"
    sql_query5 = "select * FROM `l2_transport` WHERE `trans_name` ='247路' AND `district_id` =2372  AND `trans_type` =4 and `level` =8"
    sql_list.append(sql_query1)
    sql_list.append(sql_query2)
    sql_list.append(sql_query3)
    sql_list.append(sql_query4)
    sql_list.append(sql_query5)
    for sql_query in sql_list:
        trans_list = pd.read_sql_query(sql_query, con=engine).values
        for trans_item in trans_list:
            trans_id = trans_item[0]
            query_l2_parent(trans_id)


check()
