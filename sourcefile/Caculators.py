#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : Caculators.py
@Author: Grace
@Date  : 2018/11/29
@Desc  : 
'''

# import modules
from math import sqrt
from math import exp
# global variables

# class definition

# function definition
def height_distinguish(fn):
    if fn.getHeight2() == -1.0:
        # 只有一个峰值的模糊数
        return 0
    else:
        # 两个峰值的模糊数
        return -1

def simlarity_caculator1(fnwh, level_fn):
    # WeiChen 2009
    print '--------caculator1----------'
    if height_distinguish(fnwh)==-1 or height_distinguish(level_fn)==-1:
        return 'None'
    pA = fnwh.getPerimeters()
    pB = level_fn.getPerimeters()
    aA = fnwh.getArea()
    aB = level_fn.getArea()
    hA = fnwh.getHeight()
    hB = level_fn.getHeight()

    # print 'A 面积：', aA
    # print 'A 边缘：', pA
    # print 'A 峰值：', hA
    # print 'B 面积：', aB
    # print 'B 边缘：', pB
    # print 'B 峰值：', hB

    res = 0
    for i, j in zip(fnwh.fuzzy_number, level_fn.fuzzy_number):
        res = res + abs(i - j)
    div1 = len(fnwh.fuzzy_number)
    div2 = max(pA, pB) + max(hA, hB)
    if div2 == 0:
        return 'None'
    else:
        similarity = (1 - res / div1) * ((min(pA, pB) + min(hA, hB)) / div2)
        return similarity




def simlarity_caculator2(fnwh, level_fn):
    # Hejazi 2010
    print '--------caculator2----------'
    if height_distinguish(fnwh)==-1 or height_distinguish(level_fn)==-1:
        return 'None'
    pA = fnwh.getPerimeters()
    pB = level_fn.getPerimeters()
    aA = fnwh.getArea()
    aB = level_fn.getArea()
    hA = fnwh.getHeight()
    hB = level_fn.getHeight()
    res = 0
    for i, j in zip(fnwh.fuzzy_number, level_fn.fuzzy_number):
        res = res + abs(i - j)
    div1 = len(fnwh.fuzzy_number)
    div2 = max(pA, pB)
    div3 = max(aA, aB) + max(hA, hB)
    if div1 == 0 or div2 == 2 or div3 == 0:
        return 'None'
    else:
        simlarity = (1 - res / div1) * (min(pA, pB) / div2) * ((min(aA, aB) + min(hA, hB)) / div3)
        return simlarity

def simlarity_caculator3(fnwh, level_fn):
    # XuZ 2011 COG optimization
    print '--------caculator3----------'
    if height_distinguish(fnwh)==-1 or height_distinguish(level_fn)==-1:
        return 'None'
    a1 = fnwh.fuzzy_number[0]
    a2 = fnwh.fuzzy_number[1]
    a3 = fnwh.fuzzy_number[2]
    a4 = fnwh.fuzzy_number[3]

    b1 = level_fn.fuzzy_number[0]
    b2 = level_fn.fuzzy_number[1]
    b3 = level_fn.fuzzy_number[2]
    b4 = level_fn.fuzzy_number[3]


    hA = fnwh.getHeight()
    hB = level_fn.getHeight()

    # print 'A 面积：', aA
    # print 'A 边缘：', pA
    # print 'A 峰值：', hA
    # print 'B 面积：', aB
    # print 'B 边缘：', pB
    # print 'B 峰值：', hB

    res = 0
    for i, j in zip(fnwh.fuzzy_number, level_fn.fuzzy_number):
        res = res + abs(i - j)
    div1 = 2 * len(fnwh.fuzzy_number)

    if a1 != a4:
        yA = (hA * ((a3 - a2) / (a4 - a1) + 2)) / 6
    else:
        yA = hA / 2
    if b1 != b4:
        yB = (hB * ((b3 - b2) / (b4 - b1) + 2)) / 6
    else:
        yB = hB / 2
    if hA != 0:
        xA = (yA * (a3 + a2) + (a4 + a1) * (hA - yA)) / (2 * hA)
    else:
        xA = (a4 + a1) / 2
    if hB != 0:
        xB = (yB * (b3 + b2) + (b4 + b1) * (hB - yB)) / (2 * hB)
    else:
        xB = (b4 + b1) / 2

    parameter = 1.25
    dAB = sqrt(pow(xA - xB, 2) + pow(yA - yB, 2)) / sqrt(parameter)
    if div1 == 0:
        return 'None'
    else:
        similarity = 1 - res / div1 - dAB / 2
        return similarity


def simlarity_caculator4(fnwh, level_fn):

    # Khorshidi 2017
    print '--------caculator4----------'
    if height_distinguish(fnwh)==-1 or height_distinguish(level_fn)==-1:
        return 'None'
    a1 = fnwh.fuzzy_number[0]
    a2 = fnwh.fuzzy_number[1]
    a3 = fnwh.fuzzy_number[2]
    a4 = fnwh.fuzzy_number[3]

    b1 = level_fn.fuzzy_number[0]
    b2 = level_fn.fuzzy_number[1]
    b3 = level_fn.fuzzy_number[2]
    b4 = level_fn.fuzzy_number[3]

    pA = fnwh.getPerimeters()
    pB = level_fn.getPerimeters()
    aA = fnwh.getArea()
    aB = level_fn.getArea()
    hA = fnwh.getHeight()
    hB = level_fn.getHeight()

    res = 0
    for i, j in zip(fnwh.fuzzy_number, level_fn.fuzzy_number):
        res = res + abs(i - j)

    if a1 != a4:
        yA = (hA * ((a3 - a2) / (a4 - a1) + 2)) / 6
    else:
        yA = hA / 2
    if b1 != b4:
        yB = (hB * ((b3 - b2) / (b4 - b1) + 2)) / 6
    else:
        yB = hB / 2
    if hA != 0:
        xA = (yA * (a3 + a2) + (a4 + a1) * (hA - yA)) / (2 * hA)
    else:
        xA = (a4 + a1) / 2
    if hB != 0:
        xB = (yB * (b3 + b2) + (b4 + b1) * (hB - yB)) / (2 * hB)
    else:
        xB = (b4 + b1) / 2

    parameter = 1.25
    dAB = sqrt(pow(xA - xB, 2) + pow(yA - yB, 2)) / sqrt(parameter)

    div1 = len(fnwh.fuzzy_number)
    div2 = max(pA,pB)
    if div1 == 0:
        return 'None'
    if div2 == 0:
        tmp = 0
    else:
        tmp = abs(pA-pB)/max(pA,pB)
    similarity = (1-res/div1*dAB)*(1-(abs(aA-aB)+abs(hA-hB)+tmp)/3)
    return similarity

def tempfunc(a1,a2,a3,a4,hA,h2A):
    IxA1 = ((a2 - a1) * pow(hA, 3)) / 12
    IxA2 = ((a3 - a2) * pow(min(hA, h2A), 3)) / 3
    if hA <= h2A:
        tmp1 = hA
        tmp2 = h2A
    else:
        tmp1 = h2A
        tmp2 = hA
    IxA3 = ((a3 - a2) / 12) * (pow(tmp2, 3) - 3 * pow(tmp1, 3) + pow(tmp1, 2) * tmp2 + tmp1 * pow(tmp2, 2))
    IxA4 = ((a4 - a3) * pow(h2A, 3)) / 12
    IyA1 = (hA / 12) * (3 * pow(a2, 3) - pow(a1, 3) - pow(a1, 2) * a2 - a1 * pow(a2, 2))
    IyA23 = (hA / 3) * (pow(a3, 3) - pow(a2, 3)) + ((h2A - hA) / 12) * (
                3 * pow(a3, 3) - pow(a2, 3) - pow(a3, 2) * a2 - a3 * pow(a2, 2))
    IyA4 = (h2A / 12) * (pow(a4, 3) - 3 * pow(a3, 3) + pow(a3, 2) * a4 + a3 * pow(a4, 2))
    return IxA1,IxA2,IxA3,IxA4,IyA1,IyA23,IyA4

def simlarity_caculator5(fnwh, level_fn):
    # Chutia 2018
    # 只有这个算法可以计算两个峰值的模糊数相似性
    print '--------caculator5----------'
    if height_distinguish(fnwh)==0 or height_distinguish(level_fn)==0:
        fnwh.setHeight2(fnwh.getHeight())
        level_fn.setHeight2(level_fn.getHeight())
    fnwh.cacuPerimeters2()
    fnwh.cacuArea2()
    a1 = fnwh.fuzzy_number[0]
    a2 = fnwh.fuzzy_number[1]
    a3 = fnwh.fuzzy_number[2]
    a4 = fnwh.fuzzy_number[3]

    b1 = level_fn.fuzzy_number[0]
    b2 = level_fn.fuzzy_number[1]
    b3 = level_fn.fuzzy_number[2]
    b4 = level_fn.fuzzy_number[3]

    hA = fnwh.getHeight()
    hB = level_fn.getHeight()
    h2A = fnwh.getHeight2()
    h2B = level_fn.getHeight2()

    res = 0
    for i, j in zip(fnwh.fuzzy_number, level_fn.fuzzy_number):
        res = res + abs(i - j)



    tempres = tempfunc(a1, a2, a3, a4, hA, h2A)
    IxA1, IxA2, IxA3, IxA4, IyA1, IyA23, IyA4 = tempres[0],tempres[1],tempres[2],tempres[3],tempres[4],\
                                                tempres[5],tempres[6]

    tempres = tempfunc(b1, b2, b3, b4, hB, h2B)
    IxB1, IxB2, IxB3, IxB4, IyB1, IyB23, IyB4 = tempres[0], tempres[1], tempres[2], tempres[3], tempres[4],\
                                                tempres[5],tempres[6]

    aA = fnwh.getArea()
    aB = level_fn.getArea()
    # if (hA == h2A and a1==a2 and a2==a3 and a3==a4) or hA == h2A==0:
    if hA == h2A and a1 == a2 and a2 == a3 and a3 == a4:
    # if aA ==0:
        rxA = hA/sqrt(3)
        ryA = a1
    else:
        print 'area:**************',aA
        # aA = fnwh.getArea()
        if aA == 0 :
            return 'None'
        rxAtmp = (IxA1 + IxA2 + IxA3 + IxA4) / aA
        ryAtmp = (IyA1 + IyA23 + IyA4) / aA
        if rxAtmp < 0 or ryAtmp < 0 :
            return 'None'
        rxA = sqrt(rxAtmp)
        ryA = sqrt(ryAtmp)
    # if (hB == h2B and b1==b2 and b2==b3 and b3==b4) or hB == h2B==0:
    if hB == h2B and b1 == b2 and b2 == b3 and b3 == b4:
    # if aB==0:
        rxB = hB/ sqrt(3)
        ryB = b1
    else:
        aB = level_fn.getArea()
        if aB == 0:
            return 'None'
        rxBtmp = (IxB1 + IxB2 + IxB3 + IxB4) / aB
        ryBtmp = (IyB1 + IyB23 + IyB4) / aB
        if rxBtmp < 0 or ryBtmp < 0 :
            return 'None'
        rxB = sqrt(rxBtmp)
        ryB = sqrt(ryBtmp)

    div1 = len(fnwh.fuzzy_number)
    div2 = max(rxA,rxB)+max(ryA,ryB)
    if div1 == 0 or div2 == 0 :
        print 'div2 ======0 '
        return 'None'
    similarity = (1 - res/div1) * (1-(abs(hA-hB)+abs(h2A-h2B))/2) * ((min(rxA,rxB)+min(ryA,ryB))/div2)
    return similarity

def simlarity_caculator6(fnwh, level_fn):
    # ChutiaOptimization 2018
    # 只有这个算法可以计算两个峰值的模糊数相似性
    print '--------caculator6----------'
    if height_distinguish(fnwh)==0 or height_distinguish(level_fn)==0:
        fnwh.setHeight2(fnwh.getHeight())
        level_fn.setHeight2(level_fn.getHeight())
    fnwh.cacuPerimeters2()
    fnwh.cacuArea2()
    a1 = fnwh.fuzzy_number[0]
    a2 = fnwh.fuzzy_number[1]
    a3 = fnwh.fuzzy_number[2]
    a4 = fnwh.fuzzy_number[3]

    b1 = level_fn.fuzzy_number[0]
    b2 = level_fn.fuzzy_number[1]
    b3 = level_fn.fuzzy_number[2]
    b4 = level_fn.fuzzy_number[3]

    hA = fnwh.getHeight()
    hB = level_fn.getHeight()
    h2A = fnwh.getHeight2()
    h2B = level_fn.getHeight2()

    res = 0
    for i, j in zip(fnwh.fuzzy_number, level_fn.fuzzy_number):
        res = res + abs(i - j)



    tempres = tempfunc(a1, a2, a3, a4, hA, h2A)
    IxA1, IxA2, IxA3, IxA4, IyA1, IyA23, IyA4 = tempres[0],tempres[1],tempres[2],tempres[3],tempres[4],\
                                                tempres[5],tempres[6]

    tempres = tempfunc(b1, b2, b3, b4, hB, h2B)
    IxB1, IxB2, IxB3, IxB4, IyB1, IyB23, IyB4 = tempres[0], tempres[1], tempres[2], tempres[3], tempres[4],\
                                                tempres[5],tempres[6]

    if (hA == h2A and a1==a2 and a2==a3 and a3==a4) or hA == h2A==0:
        rxA = hA/sqrt(3)
        ryA = a1
    else:
        aA = fnwh.getArea()
        if aA == 0 :
            return 'None'
        rxAtmp = (IxA1 + IxA2 + IxA3 + IxA4) / aA
        ryAtmp = (IyA1 + IyA23 + IyA4) / aA
        if rxAtmp < 0 or ryAtmp < 0 :
            print 'genhao------'
            return 'None'
        rxA = sqrt(rxAtmp)
        ryA = sqrt(ryAtmp)
    if (hB == h2B and b1==b2 and b2==b3 and b3==b4) or hB == h2B==0:
        rxB = hB/ sqrt(3)
        ryB = b1
    else:
        aB = level_fn.getArea()
        if aB == 0:
            return 'None'
        rxBtmp = (IxB1 + IxB2 + IxB3 + IxB4) / aB
        ryBtmp = (IyB1 + IyB23 + IyB4) / aB
        if rxBtmp < 0 or ryBtmp < 0 :
            return 'None'
        rxB = sqrt(rxBtmp)
        ryB = sqrt(ryBtmp)

    div1 = len(fnwh.fuzzy_number)
    div2 = max(rxA,rxB)+max(ryA,ryB)
    if div2 == 0:
        tmp =  1
    else:
        tmp = (min(rxA,rxB)+min(ryA,ryB))/div2
    if div1 == 0 :
        return 'None'
    similarity = (1 - res/div1) * (1-(abs(hA-hB)+abs(h2A-h2B))/2) * tmp
    return similarity

def simlarity_caculator7(fnwh, level_fn):
    # chen 2001 COG
    print '--------caculator7----------'
    if height_distinguish(fnwh)==-1 or height_distinguish(level_fn)==-1:
        return 'None'
    a1 = fnwh.fuzzy_number[0]
    a2 = fnwh.fuzzy_number[1]
    a3 = fnwh.fuzzy_number[2]
    a4 = fnwh.fuzzy_number[3]

    b1 = level_fn.fuzzy_number[0]
    b2 = level_fn.fuzzy_number[1]
    b3 = level_fn.fuzzy_number[2]
    b4 = level_fn.fuzzy_number[3]

    hA = fnwh.getHeight()
    hB = level_fn.getHeight()

    sA = a4 - a1
    sB = b4 - b1

    res = 0
    for i, j in zip(fnwh.fuzzy_number, level_fn.fuzzy_number):
        res = res + abs(i - j)
    div1 = len(fnwh.fuzzy_number)

    if a1 != a4:
        yA = (hA * ((a3 - a2) / (a4 - a1) + 2)) / 6
    else:
        yA = hA / 2
    if b1 != b4:
        yB = (hB * ((b3 - b2) / (b4 - b1) + 2)) / 6
    else:
        yB = hB / 2
    if hA != 0:
        xA = (yA * (a3 + a2) + (a4 + a1) * (hA - yA)) / (2 * hA)
    else:
        xA = (a4 + a1) / 2
    if hB != 0:
        xB = (yB * (b3 + b2) + (b4 + b1) * (hB - yB)) / (2 * hB)
    else:
        xB = (b4 + b1) / 2

    div2 = max(yA,yB)
    if div1 == 0 or div2 == 0:
        return 'None'
    tmp = sA+sB
    if tmp>0:
        B = 1
    else:
        B = 0
    similarity = (1-res/div1) * pow(1-abs(xA-xB) , B) * ( min(yA,yB)/div2 )
    return similarity

def tempfunc1(a1,a2,a3,a4,hA):
    IxA1 = ((a2 - a1) * pow(hA, 3)) / 12
    IxA2 = ((a3 - a2) * pow(hA, 3)) / 3
    IxA3 = ((a4 - a3) * pow(hA, 3)) /12

    IyA1 = (pow(a2-a1,3)*hA)/4 + ((a2-a1)*pow(a1,2)*hA)/2 + (2*pow(a2-a1,2)*hA)/3
    IyA2 = (pow(a3-a2,3)*hA)/3 + (a3-a2)*pow(a2,2)*hA + pow(a3-a2,2)*a2*hA
    IyA3 = (pow(a4-a3,3)*hA)/12 + ((a4-a3)*pow(a3,2)*hA)/2 + (pow(a4-a3,2)*a3*hA)/3

    return IxA1,IxA2,IxA3,IyA1,IyA2,IyA3

def simlarity_caculator8(fnwh, level_fn):
    # 实现有问题 待修改
    # deng ROG raw
    print '--------caculator8----------'
    a1 = fnwh.fuzzy_number[0]
    a2 = fnwh.fuzzy_number[1]
    a3 = fnwh.fuzzy_number[2]
    a4 = fnwh.fuzzy_number[3]

    b1 = level_fn.fuzzy_number[0]
    b2 = level_fn.fuzzy_number[1]
    b3 = level_fn.fuzzy_number[2]
    b4 = level_fn.fuzzy_number[3]

    hA = fnwh.getHeight()
    hB = level_fn.getHeight()

    sA = a4 - a1
    sB = b4 - b1

    res = 0
    for i, j in zip(fnwh.fuzzy_number, level_fn.fuzzy_number):
        res = res + abs(i - j)
    div1 = len(fnwh.fuzzy_number)

    tempres = tempfunc1(a1, a2, a3, a4, hA)
    IxA1, IxA2, IxA3,IyA1, IyA2, IyA3 = tempres[0], tempres[1], tempres[2], tempres[3], tempres[4], tempres[5]

    tempres = tempfunc1(b1, b2, b3, b4, hB)
    IxB1, IxB2, IxB3,IyB1, IyB2, IyB3 = tempres[0], tempres[1], tempres[2], tempres[3], tempres[4], tempres[5]


    if fnwh.getArea()==0:
        rxA = hA/sqrt(3)
        ryA = a1
    else:
        rxA = sqrt((IxA1 + IxA2 + IyA3) / (((a3 - a2 + a4 - a1) * hA) / 2))
        ryA = sqrt((IyA1 + IyA2 + IyA3) / (((a3 - a2 + a4 - a1) * hA) / 2))
    if level_fn.getArea()==0:
        rxB = hB/ sqrt(3)
        ryB = b1
    else:
        rxB = sqrt((IxB1+IxB2+IyB3)/(((b3-b2+b4-b1)*hB)/2))
        ryB = sqrt((IyB1+IyB2+IyB3)/(((b3-b2+b4-b1)*hB)/2))

    div2 = max(ryA, ryB)
    if div1 == 0 or div2 == 0:
        return 'None'
    tmp = sA + sB
    if tmp > 0:
        B = 1
    else:
        B = 0
    similarity = (1 - res / div1) * pow(1 - abs( rxA -rxB ), B) * (min(ryA, ryB) / div2)
    return similarity


def simlarity_caculator9(fnwh, level_fn):
    # Chutia opt2
    # 只有这个算法可以计算两个峰值的模糊数相似性
    print '--------caculator9----------'
    if height_distinguish(fnwh)==0 or height_distinguish(level_fn)==0:
        fnwh.setHeight2(fnwh.getHeight())
        level_fn.setHeight2(level_fn.getHeight())
    fnwh.cacuPerimeters2()
    fnwh.cacuArea2()
    a1 = fnwh.fuzzy_number[0]
    a2 = fnwh.fuzzy_number[1]
    a3 = fnwh.fuzzy_number[2]
    a4 = fnwh.fuzzy_number[3]

    b1 = level_fn.fuzzy_number[0]
    b2 = level_fn.fuzzy_number[1]
    b3 = level_fn.fuzzy_number[2]
    b4 = level_fn.fuzzy_number[3]

    hA = fnwh.getHeight()
    hB = level_fn.getHeight()
    h2A = fnwh.getHeight2()
    h2B = level_fn.getHeight2()

    res = 0
    for i, j in zip(fnwh.fuzzy_number, level_fn.fuzzy_number):
        res = res + abs(i - j)



    tempres = tempfunc(a1, a2, a3, a4, hA, h2A)
    IxA1, IxA2, IxA3, IxA4, IyA1, IyA23, IyA4 = tempres[0],tempres[1],tempres[2],tempres[3],tempres[4],\
                                                tempres[5],tempres[6]

    tempres = tempfunc(b1, b2, b3, b4, hB, h2B)
    IxB1, IxB2, IxB3, IxB4, IyB1, IyB23, IyB4 = tempres[0], tempres[1], tempres[2], tempres[3], tempres[4],\
                                                tempres[5],tempres[6]

    aA = fnwh.getArea()
    aB= level_fn.getArea()

    # if (hA == h2A and a1==a2 and a2==a3 and a3==a4) or hA == h2A==0:
    if a1 == a2 and a2 == a3 and a3 == a4 :
    # 1）abcd相等，垂直于x轴的线段（有可能和y轴重合） or x轴上的一个点
        rxA = hA/sqrt(3)
        ryA = a1
    elif hA == 0 and a1 != a4:
    # 2）峰值为0，x轴上的一个线段
        rxA = 0
        ryA = sqrt((pow(a1,2)+pow(a4,2)+a1*a4)/3)
    else:
        print 'area:**************',aA
        # aA = fnwh.getArea()
        # if aA == 0 :
        #     return 'None'
        rxAtmp = (IxA1 + IxA2 + IxA3 + IxA4) / aA
        ryAtmp = (IyA1 + IyA23 + IyA4) / aA
        if rxAtmp < 0 or ryAtmp < 0 :
            return 'None'
        rxA = sqrt(rxAtmp)
        ryA = sqrt(ryAtmp)

    # if (hB == h2B and b1==b2 and b2==b3 and b3==b4) or hB == h2B==0:
    if b1 == b2 and b2 == b3 and b3 == b4:
    # 1）abcd相等，垂直于x轴的线段（有可能和y轴重合） or x轴上的一个点
        rxB = hB/ sqrt(3)
        ryB = b1
    elif hB == 0 and b1 != b4:
    # 2）峰值为0，x轴上的一个线段
        rxB = 0
        ryB = sqrt((pow(b1,2)+pow(b4,2)+b1*b4)/3)

    else:
        # aB = level_fn.getArea()
        # if aB == 0:
        #     return 'None'
        rxBtmp = (IxB1 + IxB2 + IxB3 + IxB4) / aB
        ryBtmp = (IyB1 + IyB23 + IyB4) / aB
        if rxBtmp < 0 or ryBtmp < 0 :
            return 'None'
        rxB = sqrt(rxBtmp)
        ryB = sqrt(ryBtmp)

    div1 = len(fnwh.fuzzy_number)
    div2 = max(rxA,rxB)+max(ryA,ryB)
    if div1 == 0 :
        return 'None'

    constraint = 0.0001
    p = (constraint+min(rxA,rxB)+min(ryA,ryB))/(constraint+div2)
    x = res/div1 + (abs(hA-hB)+abs(h2A-h2B))/2 + (1-p)

    similarity = exp(-x)
    return similarity

# main function
if __name__ == '__main__':
    pass
