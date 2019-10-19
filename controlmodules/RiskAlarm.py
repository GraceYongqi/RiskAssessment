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
    print "receiver:" ,rcv
# function definition
def riskAlarm(level):
    # 将原始level映射到低中高三个等级
    # 低危：3-5； 中危：6-7；高危：8-9
    # 根据config文件中的推送方式进行推送
    isSend = ReadConfig.readSend(level)[0]
    receiver = ReadConfig.readSend(level)[1]
    target = []
    if isSend == "0":
        pass
    elif isSend == "1":
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
