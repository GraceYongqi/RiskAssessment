#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : RiskAlarm.py
@Author: Grace
@Date  : 2019/9/23
@Desc  : 
'''

# import modules
import RiskManagement
import ReadConfig
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# global variables
alarm_levels = ['fairly high', 'high', 'very high', 'absolutely high']
# class definition

# 设置SMTP服务器以及登录信息
SERVER = {
    'host': "smtp.qq.com",
    'port': 465
}

USER = {
    "email": "981827572@qq.com",  # 邮箱登录账号
    "password": "Yq960526."  # 发送人邮箱的授权码
}


class PersonMail(object):
    def __init__(self, receivers, sender=USER["email"]):
        self.From = sender
        self.To = receivers
        self.msg = ''

    def write_msg(self, subject, content):
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        self.msg = MIMEText(content, 'plain', 'utf-8')
        self.msg['From'] = Header(self.From)
        self.msg['To'] = Header(str(";".join(self.To)))
        self.msg['Subject'] = Header(subject)

    def send_email(self):
        try:
            smtp_client = smtplib.SMTP_SSL(SERVER["host"], SERVER["port"])
            smtp_client.login(USER["email"], USER["password"])
            smtp_client.sendmail(self.From, self.To, self.msg.as_string())
            smtp_client.quit()
            return 1
        except smtplib.SMTPException as e:
            print("error", e)
            return 0

def sendAlarm(receivers):
    print "receiver:" ,receivers
    # ReadConfig.readContacts(receivers)
    # pengpeng_email = PersonMail(receivers)
    # pengpeng_email.write_msg("alarm!", "login in system to check")
    # result = pengpeng_email.send_email()
    # print(result)

# function definition
def riskAlarm(level):
    # 将原始level映射到低中高三个等级
    # 低危：3-5； 中危：6-7；高危：8-9
    # 根据config文件中的推送方式进行推送
    print "level:", level
    isSend = int(ReadConfig.readSend(level)[0])
    receiver = int(ReadConfig.readSend(level)[1])
    target = []
    if isSend == 0:
        pass
    elif isSend == 1:
        if receiver == 0:
            target = None
        elif receiver == 1:
            target = ["normal"]
        elif receiver == 2:
            target = ["normal","root"]
    sendAlarm(target)

# main function
if __name__ == '__main__':
    pass
