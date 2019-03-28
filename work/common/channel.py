# coding=utf-8

# l2级库支持的数据源渠道
# 31 - 链家
# 43 - 安居客
# 41 - 房天下
# 42 - 嗨住
# 35 - 中原地产
# 44 - 蘑菇
# 34 - 巴乐兔
# 28 - 58
# 40 - 贝壳
# 53 - 家在上海
# 38 - 58公寓
# 45 - 百姓网
# 47 - 青客
# 46 - Q房网
# 37 - 赶集网
# 54 - 我爱我家
# 20 - 蛋壳公寓
# 57 - 优客逸家
# 39 - 乐居租房
# 55 - 爱租哪
# 62 - 爱上租
# 61 - 悟空找房
# 21 - 自如
channel_spider = [21, 31, 28, 61, 62, 55, 39, 57, 20, 54, 37, 47, 45, 38, 53, 40, 35, 42, 41, 43, 44, 34, 46]
# 6666 - 自平台
# 6667 - 自平台 托管
# 6668 - 自平台 导入
channel_self = [6666, 6667, 6668]
# l1级数据分表渠道分城市对应的房源表
table_l1_house = {
    0: {
        0: 'house_info',
        2: 'house_info_2',
        802: 'house_info_802',
        1965: 'house_info_1965',
        1988: 'house_info_1988',
        934: 'house_info_934',
        2368: 'house_info_2368'
    },
    31: {
        0: 'house_info_c31',
        2: 'house_info_c31_2',
        802: 'house_info_c31_802',
        1965: 'house_info_c31_1965',
        1988: 'house_info_c31_1988',
        934: 'house_info_c31_934',
        2368: 'house_info_c31_2368'
    },
    28: {
        0: 'house_info_c28',
        2: 'house_info_c28_2',
        802: 'house_info_c28_802',
        1965: 'house_info_c28_1965',
        1988: 'house_info_c28_1988',
        934: 'house_info_c28_934',
        2368: 'house_info_c28_2368'
    },
    41: {
        0: 'house_info_c41',
        2: 'house_info_c41_2',
        802: 'house_info_c41_802',
        1965: 'house_info_c41_1965',
        1988: 'house_info_c41_1988',
        934: 'house_info_c41_934',
        2368: 'house_info_c41_2368'
    },
    37: {
        0: 'house_info_c37',
        2: 'house_info_c37_2',
        802: 'house_info_c37_802',
        1965: 'house_info_c37_1965',
        1988: 'house_info_c37_1988',
        934: 'house_info_c37_934',
        2368: 'house_info_c37_2368'
    },
    34: {
        0: 'house_info_c34',
        2: 'house_info_c34_2',
        802: 'house_info_c34_802',
        1965: 'house_info_c34_1965',
        1988: 'house_info_c34_1988',
        934: 'house_info_c34_934',
        2368: 'house_info_c34_2368'
    },
    40: {
        0: 'house_info_c40',
        2: 'house_info_c40_2',
        802: 'house_info_c40_802',
        1965: 'house_info_c40_1965',
        1988: 'house_info_c40_1988',
        934: 'house_info_c40_934',
        2368: 'house_info_c40_2368'
    }
}
# l1级数据分表渠道分城市对应的图片表
table_l1_pic = {
    0: {
        0: 'house_pic',
        2: 'house_pic_2',
        802: 'house_pic_802',
        1965: 'house_pic_1965',
        1988: 'house_pic_1988',
        934: 'house_pic_934',
        2368: 'house_pic_2368'
    },
    31: {
        0: 'house_pic_c31',
        2: 'house_pic_c31_2',
        802: 'house_pic_c31_802',
        1965: 'house_pic_c31_1965',
        1988: 'house_pic_c31_1988',
        934: 'house_pic_c31_934',
        2368: 'house_pic_c31_2368'
    },
    28: {
        0: 'house_pic_c28',
        2: 'house_pic_c28_2',
        802: 'house_pic_c28_802',
        1965: 'house_pic_c28_1965',
        1988: 'house_pic_c28_1988',
        934: 'house_pic_c28_934',
        2368: 'house_pic_c28_2368'
    },
    41: {
        0: 'house_pic_c41',
        2: 'house_pic_c41_2',
        802: 'house_pic_c41_802',
        1965: 'house_pic_c41_1965',
        1988: 'house_pic_c41_1988',
        934: 'house_pic_c41_934',
        2368: 'house_pic_c41_2368'
    },
    37: {
        0: 'house_pic_c37',
        2: 'house_pic_c37_2',
        802: 'house_pic_c37_802',
        1965: 'house_pic_c37_1965',
        1988: 'house_pic_c37_1988',
        934: 'house_pic_c37_934',
        2368: 'house_pic_c37_2368'
    },
    34: {
        0: 'house_pic_c34',
        2: 'house_pic_c34_2',
        802: 'house_pic_c34_802',
        1965: 'house_pic_c34_1965',
        1988: 'house_pic_c34_1988',
        934: 'house_pic_c34_934',
        2368: 'house_pic_c34_2368'
    },
    40: {
        0: 'house_pic_c40',
        2: 'house_pic_c40_2',
        802: 'house_pic_c40_802',
        1965: 'house_pic_c40_1965',
        1988: 'house_pic_c40_1988',
        934: 'house_pic_c40_934',
        2368: 'house_pic_c40_2368'
    }
}
# l2级数据分城市对应的房源表
table_l2_house = {
    0: 'l2_house_sp',
    2: 'l2_house_sp_2',
    802: 'l2_house_sp_802',
    1965: 'l2_house_sp_1965',
    1988: 'l2_house_sp_1988',
    934: 'l2_house_sp_934',
    2368: 'l2_house_sp_2368'
}
# l2级数据分城市对应的瓦片表
table_l2_tile = {
    2: 'l2_tile_2',
    802: 'l2_tile_802',
    1965: 'l2_tile_1965',
    1988: 'l2_tile_1988',
    934: 'l2_tile_934',
    2368: 'l2_tile_2368'
}
# l2级数据分城市对应的瓦片表
table_l3_cluster_record = {
    2: 'l3_cluster_record_2',
    802: 'l3_cluster_record_802',
    1965: 'l3_cluster_record_1965',
    1988: 'l3_cluster_record_1988',
    934: 'l3_cluster_record_934',
    2368: 'l3_cluster_record_2368'
}
