#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/03 17:25
# @Author  : zc
# @File    : mail.py



import yagmail

yag = yagmail.SMTP(user="zhangchanget@126.com",password="XXX",host="smtp.126.com")

contents = ["群发邮件测试","看看list里到底都是邮件哪一部分","哈哈哈哈list第三"]

# yag.send('272932709@qq.com',"subject主题？",contents) #不带附件
# yag.send('272932709@qq.com',"subject主题+附件",contents,["E://青青子佩//图片//1.jpg"]) #带附件
yag.send('943102912@qq.com',"subject主题",contents)  #多个收件人