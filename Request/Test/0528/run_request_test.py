#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/28 11:55
# @Author  : zc
# @File    : run_request_test.py

import unittest
import os
import time
import yagmail
from BSTestRunner import BSTestRunner

from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from email.mime.text import MIMEText

def getNewReport(report_url):
    '''
    获取最新生成的测试报告
    :param report_url:
    :return:
    '''
    lists = os.listdir(report_url)
    lists.sort(key= lambda fn: os.path.getmtime(report_url + fn))
    newReport = os.path.join(report_url,lists[-1])
    return newReport


def sendYagMail(report_path):
    '''发送报告'''
    sendmail = 'zhangchanget@126.com'
    sendpswd = 'XXX'
    receivemail = '943102912@qq.com'

    # 连接邮箱服务器
    yag = yagmail.SMTP(user=sendmail, password=sendpswd, host='smtp.126.com')
    # ②发送html邮件正文
    # 读取邮件模板
    # file_object = open(newReport)
    # try:
    #     contentsbody = file_object.read()
    # finally:
    #     file_object.close()
    # contents = contentsbody
    contents = ["发送邮件"]

    # 附件地址
    fujian = [report_path]
    # 发送邮件附件
    try:
        yag.send(receivemail,'《自动化报告》', contents, fujian)
    except ConnectionResetError:
        pass
    yag.close()
    time.sleep(1)



def sendMail(newReport,report_name):
    '''
    ①普通发送邮件
    :param newReport:
    :param report_name:
    :return:
    '''
    sendMail = 'zhangchanget@126.com'
    sendpswd = 'XXX'
    receiveMail = '943102912@qq.com'


    # 创建邮件信息
    msg = MIMEMultipart()
    # 读取最新报告文件
    f = open(newReport,'rb').read()
    # 设置邮件主体
    mailBody =  MIMEText(f,'html','utf-8')
    # 邮件主体放入到消息中
    msg.attach(mailBody)
    # 邮件标题
    msg['Subject'] = Header("《自动化测试报告邮件》",'utf-8')
    msg['From'] = sendMail
    msg['To'] = receiveMail

    # 邮件附件
    att = MIMEApplication(f)
    att['Content-Type'] = 'application/octet-stream'
    att.add_header('Content-Disposition','attachment',filename=report_name)
    msg.attach(att)


    smtp = SMTP()
    # 连接邮箱
    smtp.connect('smtp.126.com')
    # 邮箱登录
    smtp.login(sendMail,sendpswd)
    # 发送邮件
    smtp.sendmail(sendMail,receiveMail,msg.as_string())



if __name__ == '__main__':

    # 基础路径
    base_path = os.path.dirname(os.path.abspath(__file__))
    # 获取当前日期
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    # 报告路径
    report_path = base_path + "/report/"
    # 报告文件路径
    report_file_path = report_path + now +"_report.html"

    # 生成报告文件
    fp = open(report_file_path,'wb')
    # 报告中填写内容
    runner = BSTestRunner(stream=fp,title="接口测试报告：",description='执行下面的用例：')
    # 执行测试用例
    discover = unittest.defaultTestLoader.discover(start_dir=base_path,pattern="test*.py")
    # 把测试用例结果返到报告中
    runner.run(discover)

    # 关闭文件
    fp.close()


    # 获取最新的report文件
    newReport = getNewReport(report_path)

    # 发送邮件
    # sendMail(newReport,"123.html")
    sendYagMail(report_file_path)

