#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : ExcuteFile.py
@Author: Grace
@Date  : 2018/11/8
@Desc  : 
'''

# import modules
from RiskFactor import riskFactor

# global variables

# class definition

# function definition

# main function
if __name__ == '__main__':
    #  待补充 父节点
    #  读取csv，输出到csv
    RF = riskFactor(None)
    RF.setProbImp(prob='HIGH'.lower(),imp = 'moderate'.lower())
    print(RF.getRiskscore())

