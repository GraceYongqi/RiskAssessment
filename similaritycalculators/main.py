#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : main.py
@Author: Grace
@Date  : 2018/11/27
@Desc  : 
'''

# import modules
import sys
# import imp
# FuzzyNumber = imp.load_source('/Users/yongqi/PycharmProjects/RiskAssessment/sourcefile/FuzzyNumber.py')
import sys
sys.path.append("../")
import sourcefile.FuzzyNumber as FuzzyNumber
from prettytable import PrettyTable
from prettytable import MSWORD_FRIENDLY
import gc
from sourcefile.PrepareFile import precision

# global variables
# file_path = '/Users/yongqi/PycharmProjects/RiskAssessment/inputfile/dataset/fuzzywithheight.csv'
# file_path = '/Users/yongqi/PycharmProjects/RiskAssessment/inputfile/dataset/analysis_data.csv'
# file_path = '/Users/yongqi/PycharmProjects/RiskAssessment/inputfile/dataset/fnwhForChutia.csv'
# file_path = '/Users/yongqi/PycharmProjects/RiskAssessment/inputfile/dataset/fnwhForOptimization.csv'
file_path = '/Users/yongqi/PycharmProjects/RiskAssessment/inputfile/dataset/analysis_data_final.csv'

# class definition

# function definition

# main function
if __name__ == '__main__':
    # 读取数据集
    # 每一行对应一个FuzzyNumber
    # 每两行成对计算相似性
    similarity_table = PrettyTable(['Data     ','A&B','Wei','Hejazi','Chen','Xu','Khorshidi','Chutia','Chutia optimization2'])
    similarity_table.add_row(['------------','-----------', '----------','--------','--------','--------','------------','--------','-------------'])
    # similarity_table = PrettyTable(['Data     ','A&B','Chutia','Chutia optimization'])
    # similarity_table.add_row(['--------','------------','--------','-------------'])

    set = []
    raw_pair = []
    with open(file_path,'r') as inputfile:
        for (index,line) in enumerate(inputfile):
            splitres = [float(f) for f in line.split(',')]
            if len(splitres) == 5:
                fn = FuzzyNumber.fnWithHeight(splitres[0:4],splitres[4])
            else:
                # 针对有两个峰值
                fn = FuzzyNumber.fnWithHeight(splitres[0:4],splitres[4],splitres[5])
            raw_pair.append(fn)
            if index & 1 == 1:
                # 奇数行，完成读取一对
                set.append(raw_pair)
                # raw_pair.clear() python3的方法
                raw_pair = []

    count = 1
    for pair in set:
        print count

        # WeiChen 2009
        similarity1 = FuzzyNumber.simlarity_caculator1(pair[0],pair[1])
        # Hejazi 2010
        similarity2 = FuzzyNumber.simlarity_caculator2(pair[0],pair[1])
        # XuZ 2011 COG optimization
        similarity3 = FuzzyNumber.simlarity_caculator3(pair[0],pair[1])
        # Khorshidi 2017
        similarity4 = FuzzyNumber.simlarity_caculator4(pair[0],pair[1])
        # chen 2001 COG
        similarity7 = FuzzyNumber.simlarity_caculator7(pair[0],pair[1])
        # 实现有问题 待修改
        # deng ROG raw
        # similarity8 = FuzzyNumber.simlarity_caculator8(pair[0],pair[1])
# 多峰值的计算必须在最后
        # Chutia 2018
        similarity5 = FuzzyNumber.simlarity_caculator5(pair[0], pair[1])
        # ChutiaOptimization 2018
        # similarity6 = FuzzyNumber.simlarity_caculator6(pair[0], pair[1])

        # ChutiaOptimization2 2018
        similarity9 = FuzzyNumber.simlarity_caculator9(pair[0], pair[1])


        fn1 = pair[0].fuzzy_number
        fn2 = pair[1].fuzzy_number
        if pair[0].getHeight2()==-1.000:
            tmp1 = pair[0].getHeight()
        else:
            tmp1 = pair[0].getHeight2()
        if pair[1].getHeight2()==-1.000:
            tmp2 = pair[1].getHeight()
        else:
            tmp2 = pair[1].getHeight2()

        similarity_table.add_row([count,'[%.3f,%.3f,%.3f,%.3f;%.3f,%.3f] \n [%.3f,%.3f,%.3f,%.3f;%.3f,%.3f]'%
                                  (fn1[0],fn1[1],fn1[2],fn1[3],pair[0].getHeight(),tmp1,
                                   fn2[0],fn2[1],fn2[2],fn2[3],pair[1].getHeight(),tmp2),
                                                            similarity1,similarity2,similarity7,similarity3,similarity4,similarity5,similarity9])
        # similarity_table.add_row([count,'[%.3f,%.3f,%.3f,%.3f;%.3f,%.3f] \n [%.3f,%.3f,%.3f,%.3f;%.3f,%.3f]'%
        #                           (fn1[0],fn1[1],fn1[2],fn1[3],pair[0].getHeight(),tmp1,
        #                            fn2[0],fn2[1],fn2[2],fn2[3],pair[1].getHeight(),tmp2),
        #                                                     similarity5,similarity6])

        count +=1

    similarity_table.border = 0
    similarity_table.set_style(MSWORD_FRIENDLY)
    # print(similarity_table)

    # 覆盖原文件（a+追加）
    with open("/Users/yongqi/PycharmProjects/RiskAssessment/outfile/analysis_out.csv", "w+") as similarity_out:
        similarity_out.write(str(similarity_table))
