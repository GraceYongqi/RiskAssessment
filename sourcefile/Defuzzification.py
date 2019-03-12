#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : Defuzzification.py
@Author: Grace
@Date  : 2018/11/13
@Desc  : 根据模糊数的不同模型选用去模糊化的算法
'''

# import modules

# global variables

# class definition

# function definition
def triangle_defuzzification(fuzzy):
    '''
    三角模糊数去模糊化
    :param fuzzy:
    :return accurate:
    '''
    accurate = sum(fuzzy) / 3
    return accurate


def trapezoidal_defuzzification(fuzzy):
    '''
    梯形模糊数去模糊化
    :param fuzzy:
    :return accurate:
    '''
    a = fuzzy[0]
    b = fuzzy[1]
    c = fuzzy[2]
    d = fuzzy[3]
    accurate = (sum(fuzzy) - ((d * c - a * b) / (d + c - a - b))) / 3
    return accurate

# main function
if __name__ == '__main__':
    pass
