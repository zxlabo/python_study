from work.common import lbs

'''
precise = 0  # 位置的附加信息，是否精确查找。1为精确查找，即准确打点；0为不精确，即模糊打点
confidence = 0  # 可信度，描述打点准确度，大于80表示误差小于100m。该字段仅作参考，返回结果准确度主要参考precise参数。
comprehension 地址理解程度。分值范围0-100，分值越大，服务对地址理解程度越高（建议以该字段作为解析结果判断标准）
'''
# item = lbs.request_baidu_location('上海市浦东新区永泰路468弄')
item = lbs.request_baidu_location('上海市泗祥路518弄')
# item = lbs.request_baidu_location('上海市嘉地中心')
# lng":121.5200646062428,"lat":31.142208441849424
lbs.do_request_baidu_address(item.lat, item.lng)

