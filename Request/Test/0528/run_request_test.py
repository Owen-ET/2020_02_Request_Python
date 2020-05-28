#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/28 11:55
# @Author  : zc
# @File    : run_request_test.py

import unittest
import os
import time
from BSTestRunner import BSTestRunner


if __name__ == '__main__':

    base_path = os.path.dirname(os.path.abspath(__file__))
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    report_path = base_path + "/report/" + now +"_report.html"

    fp = open(report_path,'wb')
    runner = BSTestRunner(stream=fp,title="接口测试报告：",description='执行下面的用例：')
    discover = unittest.defaultTestLoader.discover(start_dir=base_path,pattern="test*.py")

    runner.run(discover)

    fp.close()