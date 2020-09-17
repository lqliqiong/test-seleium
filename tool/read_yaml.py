import os

import yaml
from config import BASE_PATH


# 定义函数

def readyaml(filename):
    file_path = BASE_PATH + os.sep + "data"+ os.sep+filename
    # 定义空列表，组装测试数据
    arrs = []
    # 获取文件流
    with open(file_path, 'r', encoding="utf-8") as f:
        for datas in yaml.safe_load(f).values():
            # arrs.append(tuple(datas.values()))
            arrs.append(datas.values())
    return arrs

    # 遍历 调用yaml.safe_load(f).values()方法
    # 返回结果


if __name__ == '__main__':
    print(readyaml("../data/mp_login.yml"))
