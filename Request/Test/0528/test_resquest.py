#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/28 11:07
# @Author  : zc
# @File    : test_resquest.py

import unittest
import requests
import os
import yaml
from ddt import ddt, data, file_data, unpack

@ddt
class TestResquest(unittest.TestCase):

    def yamlData(self):
        '''获取yaml数据'''
        self.path = os.path.dirname(os.path.abspath(__file__))
        # yaml路径
        self.yamlPath = self.path + "/data/case_data.yaml"
        # 获取yaml数据
        with open(self.yamlPath, 'r', encoding='utf-8') as file:
            data = yaml.load(file)
        return data

    # @unittest.skip("不看")
    def test_request01(self):
        '''一般yaml方法'''
        #==========================旧传参写法========================
        # url = 'https://ascendas.17mine.cn/basic/pick/selectPage'
        # headers = {'Authorization':'eyJhbGciOiJIUzI1NiJ9.eyJuZWVkRWRpdCI6LTEsImxvZ2luVGltZSI6MTU5MDYyOTYwMTU0NSwibG9naW5XYXkiOjEsInVzZXJOYW1lIjoi5byg55WFIiwidXNlcklkIjoiMTI1NDI5NDE4NzAzODM0NzI2NCIsImxvZ2luU291cmNlIjotMSwiYWNjb3VudCI6IjEzNjQyMDQwNjMxIiwiZXhwIjoxNTkwNjcyODAxfQ.qydhemA3sGfrBuHFWcTi8OdaOcm7hvIpgErtkQ2OVBo'}
        # payload = {
        #     'pageNum': '1',
        #     'pageSize': '1',
        #     'user_id': '1254294187038347264',
        #     'userId': '1254294187038347264',
        #     'infos_id': '1207504682260500480',
        #     'infoId': '1207504682260500480'}
        #==========================================================

        # =======================yaml写法①=========================
        case01 = self.yamlData()['case01']
        url = case01['url']
        payload = case01['payload']
        headers = case01['headers']

        r = requests.post(url,params=payload,headers=headers).json()
        self.assertEqual(r['data']['records'][0]['stockOutName'],"0506测试仓库")

    # @unittest.skipIf(2>1,"大于不执行")
    @file_data('./data/case_data.yaml')
    @unpack
    def test_request02(self,**kwargs):
        '''DDT数据驱动yaml方法'''
        url = kwargs['url']
        payload = kwargs['payload']
        # url = 'https://www.v2ex.com/api/nodes/show.json'
        # payload = {"name":"python"}
        r = requests.get(url,params=payload).json()
        self.assertEqual(r['id'],90)

    # @unittest.skip("不看")
    def test_request03(self):
        '''无yaml方法'''
        url = "https://www.v2ex.com/api/nodes/show.json"
        querystring = {"name": "python"}
        response = requests.request("GET", url, params=querystring).json()
        self.assertEqual(response['name'], 'python')
        self.assertEqual(response['id'], 90)

if __name__ == '__main__':
    unittest.main()