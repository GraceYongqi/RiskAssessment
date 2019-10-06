#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : ReadConfig.py
@Author: Grace
@Date  : 2019/9/24
@Desc  : 
'''

# import modules
import ConfigParser

# global variables

# class definition

# function definition


def readIndex():
    cf = ConfigParser.ConfigParser()
    impacts = []
    stops = []
    cf.read('../configs/IndexOfSentiment.conf')
    stops.append(len(cf.sections()))
    cf.read('../configs/IndexOfQuality.conf')
    stops.append(len(cf.sections()))
    cf.read('../configs/IndexOfEfficiency.conf')
    stops.append(len(cf.sections()))
    cf.read('../configs/IndexOfIncorrupt.conf')
    stops.append(len(cf.sections()))
    all_indexes = map(lambda x: str(x).decode('string_escape'), cf.sections())
    for name in cf.sections():
        impacts.append(cf.get(name, "impact"))
    return all_indexes,impacts,stops

def readSend(level):
    sf = ConfigParser.ConfigParser()
    sf.read("../configs/send.conf")
    isSend = sf.get(level,"issend")
    receiver = sf.get(level,"receiver")
    return isSend,receiver

# main function
if __name__ == '__main__':
    print readIndex()[0],readIndex()[1],readIndex()[2]
    print readSend("low")
