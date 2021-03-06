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
    cf.read('../configs/1.conf')
    stops.append(len(cf.sections()))
    cf.read('../configs/2.conf')
    stops.append(len(cf.sections()))
    cf.read('../configs/3.conf')
    stops.append(len(cf.sections()))
    cf.read('../configs/4.conf')
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

def readContacts(rcvs):
    of = ConfigParser.ConfigParser()
    of.read("../configs/contacts.conf")
    result = []
    for rcv in rcvs:
        res = of.get(rcv,"mail")
        for i in res:
            result.append(i)
    return result

# main function
if __name__ == '__main__':
    print readIndex()[0],readIndex()[1],readIndex()[2]
    print readSend("low")
