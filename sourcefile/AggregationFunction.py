#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : AggregationFunction.py
@Author: Grace
@Date  : 2019/6/4
@Desc  : 
'''

# import modules
import copy
import InputFile

# global variables
size = 4
n = size - 1
# class definition

# function definition
# PFWA
def PFWA(R, W,alpha):
    # do something
    a = 0.000
    b = 0.000

    # R = [[a,b,c,d],[a,b,c,d]...] //W
    # PrepareFile中有模糊数形式，第4个元素是权值
    # 抽出三个区间值进行PWFA计算

    # 只算边上两个区间值对应的结果为min和max
    # 把R 两个区间值全部抽出来形成两个列表[a1,a2,a3,a4...]&[b1,b2,b3...]
    # W中的区间值也抽出来 [c1,c2,c3...]&[d1,d2,d3...]
    for r in R:
        if r[0]!=r[1] and r[0]!=r[2] and r[1]!=r[2]:
            r[0] = (alpha - (r[3]*r[0])/(r[0]-r[1]))/(r[3]/(r[1]-r[0]))
            r[2] = (alpha - (r[3]*r[2])/(r[2]-r[1]))/(r[3]/(r[1]-r[2]))
        elif r[0]!=r[1] and r[1]==r[2]:
            r[0] = (alpha - (r[3] * r[0]) / (r[0] - r[1])) / (r[3] / (r[1] - r[0]))
            r[2] = r[2]
        elif r[0]==r[1] and r[1]!=r[2]:
            r[0] = r[0]
            r[2] = (alpha - (r[3]*r[2])/(r[2]-r[1]))/(r[3]/(r[1]-r[2]))
        elif r[0] == r[1] == r[2]:
            pass


    A = []
    B = []
    C = []
    D = []
    for t in R:
        A.append(float(t[0]))
        B.append(float(t[2]))
    for t in W:
        C.append(float(t[0]))
        D.append(float(t[2]))
    EC = copy.deepcopy(C)
    FD = copy.deepcopy(D)

    # 根据alpha修改区间值

    # print len(EC)
    new_a = 0.000
    new_b = 0.000
    new_w = 0.000
    new_wb = 0.000
    for i in range(n):
    # def getNewVlaue(A , B, C , D, EC, FD ):

        # if len(A)>1:
        a1 = max(A)
        an = min(A)
        mark_low = mark_high = 0
        for index,tmp_a in enumerate(A):
            if tmp_a == an:
                mark_low = index
        cn = C[mark_low]
        dn = D[mark_low]

        # 删掉一个元素后，列表长度、index值会变
        del A[mark_low]
        del C[mark_low]
        del D[mark_low]

        for index, tmp_a in enumerate(A):
            if tmp_a == a1:
                mark_high = index
        c1 = C[mark_high]
        d1 = D[mark_high]
        del A[mark_high]
        del C[mark_high]
        del D[mark_high]

        # print 'c1:',c1
        # print 'dn:',dn
        if new_w == new_wb == 0.000:
            pass
        else:
            c1 = new_w
            dn = new_w
        new_a = (a1*c1+an*dn)/(c1+dn)
        new_w = c1+dn
        new_c = new_d = new_w
        A.append(new_a)
        C.append(new_c)
        D.append(new_d)

        # if len(B) > 1:
        b1 = max(B)
        bn = min(B)

        mark_low_B = mark_high_B = 0

        for index,tmp_b in enumerate(B):
            if tmp_b == bn:
                mark_low_B = index
        # print len(EC)
        # print 'mark_low_B:',mark_low_B
        ecn = EC[mark_low_B]
        fdn = FD[mark_low_B]
        del B[mark_low_B]
        del EC[mark_low_B]
        del FD[mark_low_B]

        for index, tmp_b in enumerate(B):
            if tmp_b == b1:
                mark_high_B = index
        ec1 = EC[mark_high_B]
        fd1 = FD[mark_high_B]

        print 'EC:',EC
        print 'FD:',FD
        del B[mark_high_B]
        del EC[mark_high_B]
        del FD[mark_high_B]


        if fd1+ecn == 0:
            new_b = 0
        else:
                if new_w == new_wb == 0.000:
                    pass
                else:
                    fd1 = new_wb
                    ecn = new_wb

        # if new_w == new_wb == 0.000:
        #     pass
        # else:
        #     fd1 = new_wb
        #     ecn = new_wb
        # new_b = (b1 * fd1 + bn * ecn) / (fd1 + ecn)
        new_wb = fd1 + ecn
        new_ec = new_fd = new_wb
        EC.append(new_ec)
        FD.append(new_fd)

        # print 'new_a:',new_a
        # print 'new_b:',new_b
    # getNewVlaue(A, B, C, D,EC, FD)

    a = new_a
    b = new_b

    return a, b



# main function
def alphaIteration(risks):
    '''
    :param risks: risks = [[风险名称,[prob1，prob2...],[impact1,impact2...]],[风险名称,[prob1，prob2...],[impact1,impact2...]],[],... ]
    :return: aggregationResult = [[风险名称, 聚合风险值], [风险名称, 聚合风险值], ... ]
    '''
    aggregationResult = []
    # A = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    # alpha是8个权值更新迭代
    A = [0.0, 0.07, 0.23, 0.42, 0.65, 0.86, 0.97, 1.0]
    low = 0.000
    high = 0.000
    weight = 0.000
    medium = 0.000

    for risk in risks:
        '''
        针对当前风险获得它的模糊风险值 result
        '''

        R = risk[1]
        W = risk[2]

        for alpha in A:
            # 每个alpha计算一个大轮
            # print 'alpha:',alpha
            a, b = PFWA(R, W, alpha)
            if alpha == 0.0:
                low = a
                high = b
            if a == b:
                medium = a
                weight = alpha
                break
        # 适应目前模糊数的输入格式
        result = [low, medium, high, weight]
        aggregationResult.append([risk[0],result])

    return aggregationResult

if __name__ == '__main__':
    risks = InputFile.inputEval()
    # print risks
    fuzzyRisks = alphaIteration(risks)
    print fuzzyRisks