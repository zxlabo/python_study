# coding=utf-8
import datetime
import time


locus_db_table = {
    2: 'l2_locus_2',  # 北京
    802: 'l2_locus_802',  # 上海
    1965: 'l2_locus_1965',  # 广州
    1988: 'l2_locus_1988',  # 深圳
    934: 'l2_locus_934',  # 杭州
    2368: 'l2_locus_2368',  # 成都
}


# 各脚本执行记录
class ExecuteRecord:
    id = 0
    # 1-房源清洗：操作房源数/添加和更新房源数(维护状态前)/更新房源数/操作失败房源数/跳过房源数/设置在线数/设置离线数
    # 2-房源聚类：处理房源数/添加主源数/更新主源数/失败房源数/※/※/※
    # 3-图片上传：处理房源数/成功图片数/删除图片数/失败图片数/跳过图片数/※/※
    # 4-自平台同步用户：操作用户数/添加和更新用户数/※/同步失败用户数/※/※/※
    # 5-自平台图片上传：处理房源数/成功图片数/删除图片数/失败图片数/跳过图片数/※/※
    # 6-自平台同步品牌：操作品牌数/添加品牌数/※/同步失败品牌数/跳过品牌数/※/※
    # 7-自平台同步房源：操作房源数/添加和更新房源数/更新房源数/操作失败房源数/跳过房源数/※/※
    # 8-自平台聚类房源：处理房源数/添加主源数/更新主源数/失败房源数/※/※/※
    # 9-组合图片上传：处理房源数/成功图片数/删除图片数/失败图片数/跳过图片数/※/※
    record_type = 0
    city_key = ''
    execute = 0
    insert = 0
    update = 0
    failed = 0
    skip = 0
    online = 0
    offline = 0
    duration = 0
    create_time = 0

    def __init__(self, record_type):
        self.create_time = time.time()
        self.record_type = record_type

    def stopwatch(self):
        self.duration = int(time.time() - self.create_time)

    def plus_execute(self):
        self.execute += 1

    def plus_insert(self):
        self.insert += 1

    def plus_update(self):
        self.update += 1

    def plus_failed(self):
        self.failed += 1

    def plus_skip(self):
        self.skip += 1

    def plus_online(self):
        self.online += 1

    def plus_offline(self):
        self.offline += 1

    def valid(self):
        return self.record_type != 0 and len(self.city_key) > 0 and self.duration > 0 and self.create_time > 0 \
               and self.execute > 0

    def merge(self, record):
        if isinstance(record, ExecuteRecord):
            self.execute += record.execute
            self.insert += record.insert
            self.update += record.update
            self.failed += record.failed
            self.skip += record.skip
            self.online += record.online
            self.offline += record.offline
            self.duration += record.duration

    def reset(self):
        self.execute = 0
        self.insert = 0
        self.update = 0
        self.failed = 0
        self.skip = 0
        self.online = 0
        self.offline = 0
        self.duration = 0
        self.create_time = time.time()

    def output(self):
        return 'record[%d]@[%s] use[%d] second | execute[%d] insert[%d] update[%d] failed[%d] skip[%d] ' \
               'online[%d] offline[%d]' \
               % (self.record_type, self.city_key, self.duration, self.execute, self.insert, self.update,
                  self.failed, self.skip, self.online, self.offline)


class Locus:
    city_id = 0
    locus_id = 0
    house_uid = ''
    timestamp = 0
    price = 0.0
    status = 0

    def __init__(self):
        pass

    def db_table(self):
        if self.city_id in locus_db_table.keys():
            return locus_db_table[self.city_id]
        return None


class ExecutePic:
    district_id = 0
    channel_id = 0
    city_id = 0
    total_house = 0
    exe_pic = 0
    duration = 0
    update_time = 0
    key = ''

    def __init__(self, data):
        self.district_id = int(data[0])
        self.channel_id = int(data[1])
        self.city_id = int(data[2])
        self.exe_pic = int(data[3])
        self.duration = int(data[4])
        self.update_time = int(data[5])
        self.total_house = int(data[6])
        self.make_key()

    def make_key(self):
        self.key = '%d-%d' % (self.district_id, self.channel_id)


class SpiderPeriod:
    start_time = ''
    end_time = ''
    src_type = 0
    city_name = ''
    is_temp = 2
    district_name = ''

    def __init__(self, data):
        self.start_time = data[0]
        self.end_time = data[1]
        self.district_name = data[2]

    def valid(self):
        if self.end_time is None or self.start_time is None:
            return False
        try:
            # 爬取周期必须大于1分30秒才认为是有效
            return self.end_time - self.start_time > datetime.timedelta(days=0, hours=0, minutes=1, seconds=0)
        except Exception:
            return False

    def output(self):
        return '[%s] to [%s] | channel[%d] city[%s]district[%s]' \
               % (self.start_time, self.end_time, self.src_type, self.city_name, self.district_name)
