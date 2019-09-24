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
# global variables
alarm_levels = ['fairly high', 'high', 'very high', 'absolutely high']
# class definition
def sendAlarm(rcv):
    print rcv
# function definition
def riskAlarm(level):
    # 根据config文件中的推送方式进行推送
    isSend = ReadConfig.readSend(level)[0]
    receiver = ReadConfig.readSend(level)[1]
    target = []
    if isSend == "0":
        pass
    elif isSend == "1":
        if receiver == "0":
            target = None
        elif receiver == "1":
            target = ["normal"]
        elif receiver == "2":
            target = ["normal","root"]
    sendAlarm(target)

# main function
if __name__ == '__main__':
    pass
