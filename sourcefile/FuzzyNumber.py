#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : FuzzyNumber.py
@Author: Grace
@Date  : 2018/11/19
@Desc  : 
'''

# import modules
from PrepareFile import linguistic_to_fuzzy
from PrepareFile import size
from PrepareFile import precision
import Caculators
from math import sqrt
# global variables

class fnWithHeight(object):
    '''
    初始化一个带峰值的模糊数（a, b, c, d; height）
    参数：perimeters，area，height，list of fuzzy
    '''
    fuzzy_number = []
    height = 0.000
    perimeters = 0.000
    area = 0.000
    height2 = -1.000
    def __init__(self,fn,h,h2=-1.000):
        self.height = h
        self.fuzzy_number = fn
        self.height2 = h2
        if self.height2 == -1.000:
            self.cacuPerimeters()
            self.cacuArea()
        else:
            self.cacuPerimeters2()
            self.cacuArea2()

    @classmethod
    def fnWithDoubleHeight(self,fn,h,h2):
        self.height = h
        self.height2 = h2
        self.fuzzy_number = fn
        # self.cacuPerimeters2()
        # self.cacuArea2()


    def getHeight(self):
        return self.height
    def getArea(self):
        return self.area
    def getPerimeters(self):
        return self.perimeters
    def cacuPerimeters(self):

        a1 = self.fuzzy_number[0]
        a2 = self.fuzzy_number[1]
        a3 = self.fuzzy_number[2]
        a4 = self.fuzzy_number[3]
        h2 = pow(self.height,2)
        self.perimeters = sqrt(pow(a2-a1,2)+h2)+sqrt(pow(a4-a3,2)+h2)+a4-a1+a3-a2

    def cacuArea(self):
        a1 = self.fuzzy_number[0]
        a2 = self.fuzzy_number[1]
        a3 = self.fuzzy_number[2]
        a4 = self.fuzzy_number[3]
        h = self.height
        self.area = (a4-a1+a3-a2)*h/2

# 两个峰值的模糊数
    def getHeight2(self):
        return self.height2

    def cacuPerimeters2(self):
        a1 = self.fuzzy_number[0]
        a2 = self.fuzzy_number[1]
        a3 = self.fuzzy_number[2]
        a4 = self.fuzzy_number[3]
        h = pow(self.height, 2)
        h2 = pow(self.height2, 2)
        self.perimeters = sqrt(pow(a2 - a1, 2) + h) + sqrt(pow(a4 - a3, 2) + h2) + a4 - a1 + sqrt(pow(a3-a2,2)+pow(self.height2-self.height,2))

    def cacuArea2(self):
        a1 = self.fuzzy_number[0]
        a2 = self.fuzzy_number[1]
        a3 = self.fuzzy_number[2]
        a4 = self.fuzzy_number[3]
        h = self.height
        h2 = self.height2
        self.area = (h2*(a4-a2) + h*(a3-a1))/2

    def setHeight2(self,h):
        self.height2 = h

# 第十一周周报
def simlarity_caculator1(fnwh, level_fn):
    return Caculators.simlarity_caculator1(fnwh,level_fn)


def simlarity_caculator2(fnwh, level_fn):
    return Caculators.simlarity_caculator2(fnwh,level_fn)


def simlarity_caculator3(fnwh, level_fn):
    return Caculators.simlarity_caculator3(fnwh,level_fn)


def simlarity_caculator4(fnwh, level_fn):
    return Caculators.simlarity_caculator4(fnwh,level_fn)

def simlarity_caculator5(fnwh, level_fn):
    return Caculators.simlarity_caculator5(fnwh,level_fn)

def simlarity_caculator6(fnwh, level_fn):
    return Caculators.simlarity_caculator6(fnwh,level_fn)

def simlarity_caculator7(fnwh, level_fn):
    return Caculators.simlarity_caculator7(fnwh,level_fn)

def simlarity_caculator8(fnwh, level_fn):
    return Caculators.simlarity_caculator8(fnwh,level_fn)

def simlarity_caculator9(fnwh, level_fn):
    return Caculators.simlarity_caculator9(fnwh,level_fn)


# 以上是带峰值的模糊数
# 以下是不带自定义峰值的普通模糊数
# 周长、面积、相似性计算在两种模糊数种都有可能涉及
# 普通模糊数不建立对象
def init_fuzzy(linguistic_term):
    '''
    初始化一个普通的列表形式的模糊数，不带峰值高度（默认为1）
    :param linguistic_term:
    :return:
    '''
    return linguistic_to_fuzzy(linguistic_term)

# def fuzzy_plus(self,f):
def fuzzy_plus(f):
    '''
    :param f: 若干个模糊数（列表）组成的列表
    :return: 列表
    '''
    plus_res = []
    for j in range(size):
        tmp = 0
        for i in f:
            tmp = tmp+i[j]
        plus_res.append(precision(tmp,2))
    return plus_res

def fuzzywith2heights_plus(f1,f2):
    '''
    :param f: 若干个模糊数（列表）组成的列表
    :return: 列表
    '''
    plus_res = []
    for i,j in zip(f1,f2):
        plus_res.append(precision(i+j,2))
    plus_res.append(min(f1[4],f2[4]))
    plus_res.append(min(f1[5],f2[5]))
    return plus_res


# def fuzzy_weightedplus(self,f,w):
def fuzzy_weightedplus(f,w):
    '''
    :param f: 若干个模糊数组成的列表
    :param w: 多个权值组成的列表
    :return: 列表
    '''
    for i,j in (w,f):
        nm_res = []
        nm_res.append(num_multiple_fuzzy(i,j))
    weightedplus_res = fuzzy_plus(nm_res)
    return weightedplus_res

# def num_multiple_fuzzy(self,n,f):
def num_multiple_fuzzy( n, f):
    n = int(n)
    num_multiple_res = []
    for i in f:
        # num_multiple_res.append(n*i)
        num_multiple_res.append(precision(n*i,2))
    return num_multiple_res

# def fuzzy_multiple(self,f1,f2):
def fuzzy_multiple(f1,f2):
    multiple_res = []
    for i in range(len(f1)):
        multiple_res.append(precision(f1[i]*f2[i],2))

    return multiple_res

def fuzzy_division(f1,f2):
    division_res = []
    for i in range(len(f1)):
        division_res.append(precision(f1[i]/f2[i],3))
    return division_res


# function definition

# main function
if __name__ == '__main__':
    pass
