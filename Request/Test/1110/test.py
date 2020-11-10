#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/10 13:35
# @Author  : zc
# @File    : test.py

import requests
import yaml
import os


path = os.path.dirname(os.path.abspath(__file__))
yamlPath = path + "/data/zijin2-0.yaml"

with open(yamlPath,'r',encoding='utf-8') as file :
    data = yaml.load(file)


yamlData = data['addFundsPayOrder']
url = yamlData['url']
payloadStr = str(yamlData['payload'])

# B2B发送到资金管理的业务单号
list = ["FK20201110000019","FK20201110000020","FK20201110000021"]

for i in list:
    payloadDict = eval(payloadStr.replace("FK20201110000017",i))
    r = requests.post(url,params=payloadDict).json()
    print(r['msg'])