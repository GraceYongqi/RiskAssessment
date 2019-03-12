#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : CaculateConsole.py
@Author: Grace
@Date  : 2018/11/28
@Desc  : 
'''

# import modules
import sys
sys.path.append("../")
from sourcefile import FuzzyNumber
# global variables

# class definition

# function definition

# main function
if __name__ == '__main__':
    num = []
    for i in range(4):
        num.append(float(raw_input()))
    h = float(raw_input())
    tar1 = FuzzyNumber.fnWithHeight(num,h)
    num = []
    for i in range(4):
        num.append(float(raw_input()))
    h = float(raw_input())
    tar2 = FuzzyNumber.fnWithHeight(num,h)

    print 'Wei\'s caculator2',FuzzyNumber.simlarity_caculator2(tar1,tar2)
    print 'Xu\'s caculator3' ,FuzzyNumber.simlarity_caculator3(tar1,tar2)