#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/28 10:34
# @Author  : zc
# @File    : request01.py
import requests

# r = requests.get("https://ascendas.17mine.cn/basic/pick/selectPage")
# print(r.headers)


headers = {'Authorization':'eyJhbGciOiJIUzI1NiJ9.eyJuZWVkRWRpdCI6LTEsImxvZ2luVGltZSI6MTU5MDYyOTYwMTU0NSwibG9naW5XYXkiOjEsInVzZXJOYW1lIjoi5byg55WFIiwidXNlcklkIjoiMTI1NDI5NDE4NzAzODM0NzI2NCIsImxvZ2luU291cmNlIjotMSwiYWNjb3VudCI6IjEzNjQyMDQwNjMxIiwiZXhwIjoxNTkwNjcyODAxfQ.qydhemA3sGfrBuHFWcTi8OdaOcm7hvIpgErtkQ2OVBo'}
payload = {
    'pageNum': '1',
    'pageSize': '1',
    'user_id': '1254294187038347264',
    'userId': '1254294187038347264',
    'infos_id': '1207504682260500480',
    'infoId': '1207504682260500480'}
r = requests.post('https://ascendas.17mine.cn/basic/pick/selectPage',params=payload,headers=headers).json()
# print(r.text)
# print(r.json())
# print(r.status_code == requests.codes.ok)
# print(r.raise_for_status())
# print(r.cookies)
# print(r['data']['records'][0]['stockOutName'])

# r = requests.get('http://tcc.taobao.com/cc/json/mobile_tel_segment.htm',params={
#     "tel":"13642040631"
# })
# print(r.text)



text = {
	"code": 200,
	"msg": "成功",
	"data": {
		"records": [{
			"infoId": "1207504682260500480",
			"pickId": "1264844787891179520",
			"pickCode": "LL202005250039ZC",
			"pickDate": "2020-06-01",
			"pickDateStr": None,
			"stockOutId": "60",
			"stockOutName": "西青仓库",
			"stockInId": "61",
			"stockInName": "南开仓库",
			"description": "052504",
			"creater": "张畅",
			"createTime": "2020-05-25 17:04:32",
			"trailer": "张畅",
			"trailTime": "2020-05-25 17:05:06",
			"rejecter": "张畅",
			"rejectTime": None,
			"status": 5,
			"oldStatus": None,
			"outboundId": None,
			"relations": [],
			"userId": None,
			"storeId": None,
			"businessNumber": None,
			"outDate": None,
			"checkoutNumber": None,
			"token": None,
			"goods": None
		}],
		"total": 8,
		"size": 1,
		"current": 1,
		"searchCount": True,
		"pages": 8
	}
}

print(text['data']['records'][0]['stockInName'])