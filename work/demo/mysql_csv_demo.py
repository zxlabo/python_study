import pandas as pd
from sqlalchemy import create_engine
from pandas import Series, DataFrame

# sql_conn = "mysql+pymysql://root:899036c045@120.26.130.180:3306/gyj_pontus"
#
# engine = create_engine(sql_conn)

# sql_query = "SELECT COUNT(a.`house_uid`),  a.business_id_v2,b.business_name,  " \
#             "a.district_id,b.district_id as b_district_id, a.tile_x, a.tile_y FROM l2_house_sp_802 a " \
#             "LEFT JOIN l2_business_v2 b ON a.city_id= b.city_id AND a.business_id_v2= b.id " \
#             "WHERE a.district_id!= b.district_id GROUP BY a.`business_id_v2`, a.`district_id`"
# result = pd.read_sql_query(sql_query, con=engine)
# result.to_csv('a.csv', encoding='utf-8')
# df_csv = pd.read_csv('a.csv')
# df_csv.to_sql('a', engine)

data1 = {'city': ['bj','sh','hz'],
         'year': [2111,2012,2122]
         }
df = DataFrame(data=data1)
print(df)
