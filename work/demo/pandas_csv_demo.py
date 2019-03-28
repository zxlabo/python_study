import pandas as pd
from sqlalchemy import create_engine
from pandas import Series, DataFrame

# sql_conn = "mysql+pymysql://root:899036c045@120.26.130.180:3306/gyj_pontus"
#
# engine = create_engine(sql_conn)


user_name = 'root'
password = '899036c045'
host = '120.26.130.180:3306'
database_name = 'gyj_pontus'
charset = 'utf8mb4'
engine = create_engine(
    "mysql+pymysql://{}:{}@{}/{}?charset={}".format(user_name, password, host, database_name, charset))
con = engine.connect()  # 创建连接
data1 = {'city': ['北京', 'sh', 'hz'], 'year': [2111, 2012, 2122]}

df = DataFrame(data=data1)
df.to_sql(name='aa', con=con, if_exists='append', index=False)
'''
if_exists：表如果存在怎么处理
append：追加
replace：删除原表，建立新表再添加
fail：什么都不干
index=False：不插入索引index
'''
# df.to_sql('aa', engine)

# sql_query = "SELECT COUNT(a.`house_uid`),  a.business_id_v2,b.business_name,  " \
#             "a.district_id,b.district_id as b_district_id, a.tile_x, a.tile_y FROM l2_house_sp_802 a " \
#             "LEFT JOIN l2_business_v2 b ON a.city_id= b.city_id AND a.business_id_v2= b.id " \
#             "WHERE a.district_id!= b.district_id GROUP BY a.`business_id_v2`, a.`district_id`"
# result = pd.read_sql_query(sql_query, con=engine)
# result.to_csv('a.csv', encoding='utf-8')
# df_csv = pd.read_csv('a.csv')
# df_csv.to_sql('a', engine)
