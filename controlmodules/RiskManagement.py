#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : RiskManagement.py
@Author: Grace
@Date  : 2019/9/23
@Desc  : 
'''

# import modules
import ConfigParser

# global variables

levels = []
isSendEmail = 0

# class definition

# function definition
def index_management(category, name, impact, probability):
    cf = ConfigParser.ConfigParser()
    if category == 1:
        path = '../configs/IndexOfSentiment.conf'
    elif category == 2:
        path = '../configs/IndexOfQuality.conf'
    elif category == 3:
        path = '../configs/IndexOfEfficiency.conf'
    elif category == 4:
        path = '../configs/IndexOfIncorrupt.conf'
    cf.read(path)
    cf.add_section(name)
    cf.set(name, "timing", 1)
    cf.set(name, "impact", impact)
    cf.set(name, "probability", probability)
    with open(path,"w") as f:
        cf.write(f)
    return

def send_management(level, isSend,receiver):
    sf = ConfigParser.ConfigParser()
    sf.read("../configs/send.conf")
    sf.set(level,"isSend" ,isSend)
    sf.set(level,"receiver", receiver)
    with open("../configs/send.conf","w")as f:
        sf.write(f)
    print 'modify success!'


def trigger_management():
    pass

# main function
if __name__ == '__main__':
    index_management(1,"微博热搜", "high", "low")
    send_management("high", 1, 1)
