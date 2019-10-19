#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
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

score_levels = {'极其低':'absolutely low','非常低':'very low','低':'low','较低':'fairly low',
                '中等':'medium','较高':'fairly high','高':'high','非常高':'very high',
                '极其高':'absolutely high'}

risk_levels = {'低危':'low', '中危': 'medium', '高危': 'high'}

# class definition

# function definition
def index_management(category, name, impact, probability):
    cf = ConfigParser.ConfigParser()
    path = '../configs/'+str(category)+'.conf'
    impact = score_levels[str(impact)]
    probability = score_levels[str(probability)]
    # if category == 1:
    #     path = '../configs/1.conf'
    # elif category == 2:
    #     path = '../configs/2.conf'
    # elif category == 3:
    #     path = '../configs/3.conf'
    # elif category == 4:
    #     path = '../configs/4.conf'
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
    level = risk_levels[str(level)]
    sf.set(level,"isSend" ,isSend)
    sf.set(level,"receiver", receiver)
    with open("../configs/send.conf","w")as f:
        sf.write(f)
    # print 'modify success!'


def trigger_management():
    pass

# main function
if __name__ == '__main__':
    index_management(1,"微博热搜", "high", "low")
    send_management("high", 1, 1)
