# -*- coding: utf-8 -*-
import random

'''
pandas有两个核心的数据结构，基于这两种数据结构，Pandas可以对数据进行
导入、清洗、处理、统计、输出
Series：一维的序列
DataFrame：二维的表结构
'''

# dict_a = {'a': [1,2,2,3]}
# dict_b = {}
# dict_b['b'] = dict_a
# print(dict_b)
str_a = '57556767,57556785;57556767|分界岭|284,57556785|陈家|410;;'
list_a = str_a.split(';')
print(len(list_a))

# def get_update_str(metro_id_ori, metro_dest_ori, str_old, str_new):
#     list_id = metro_id_ori.split(',')
#     list_desc = metro_dest_ori.split(',')
#     for idx, item in enumerate(list_id):
#         if item.strip() == str_old:
#             list_id[idx] = str_new
#             str_desc = list_desc[idx]
#             str_update = str_desc.replace(str_old, str_new)
#             list_desc[idx] = str_update
#     str_id_update = ','.join(list_id)
#     str_desc_update = ','.join(list_desc)
#     return str_id_update, str_desc_update
#
#
# a = '57401535,57401247,57403605,57401211,57403569'
# b = '57401535|延平路余姚路|118,57401247|胶州路余姚路|184,57403605|余姚路延平路|194,57401211|余姚路胶州路|256,57403569|安远路胶州路|313'
# aa, bb = get_update_str(a, b, '57403569', '123456')
# print(aa)
# print(bb)
