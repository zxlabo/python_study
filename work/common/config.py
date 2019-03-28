import os
import json


# 根据key列表读取配置参数
def load_config(keys):
    configs = {}
    cur_path = os.path.dirname(__file__) + '/'
    with open(cur_path + '../config/config.json', 'r', encoding='utf-8') as json_file:
        json_obj = json.load(json_file)
        for key in keys:
            try:
                configs[key] = json_obj[key]
            except Exception:
                pass
    return configs
