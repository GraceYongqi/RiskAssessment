#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : other.py
@Author: Grace
@Date  : 2018/11/15
@Desc  : 
'''

# import modules

# global variables

# class definition

# function definition
def similarity_caculate(raw_original,raw_target):
    original = []
    target = []
    for i,j in raw_original,raw_target:
        if i not in original:
            original.append(i)
        if j not in target:
            target.append(j)
    len = len(target)
    if len==3:
        triangle_similarity(original,target)
    elif len==4:
        trapezoidal_similarity()

def triangle_similarity():
    pass

def trapezoidal_similarity():
    pass

class fuzzyNumber(object):
    left = middle = right = height = 0.000
    def __init__(self,left,middle,right,height):
        self.left = left
        self.middle = middle
        self.right = right
        self.height = height
    def getEqualities(self):
        k1 = self.height/(self.middle - self.left)
        b1 = self.height-k1*self.middle
        k2 = self.height/(self.right - self.middle)
        b2 = self.height-k2*self.middle

def PFWA():
    fnp1 = fuzzyNumber(0.200,0.384,0.536,0.867)
    fnp2 = fuzzyNumber(0.133,0.323,0.485,0.733)
    fnp3 = fuzzyNumber(0.443,0.581,0.667,0.800)
    fni1 = fuzzyNumber(0.323,0.485,0.605,0.867)
    fni2 = fuzzyNumber(0.528,0.629,0.667,0.733)
    fni3 = fuzzyNumber(0.491,0.613,0.658,0.800)
    alpha = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.733, 0.8, 0.867, 0.9, 1.0]
    for i in alpha:
        fnp1.getEqualities()


# main function
if __name__ == '__main__':
    pass
