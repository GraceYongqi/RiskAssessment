#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : InputFile.py
@Author: Grace
@Date  : 2018/11/8
@Desc  : 建立风险层级结构，读取专家目录，定义每个风险因素的语言描述
'''

# import modules
import os
import FuzzyNumber
from FuzzyNumber import init_fuzzy
from FuzzyNumber import fuzzy_plus
from FuzzyNumber import fuzzy_multiple
from FuzzyNumber import fuzzy_division
from RiskFactor import riskFactor
from RiskFactor import sortRisk
from PrepareFile import expert_count
# from prettytable import PrettyTable
import prettytable
from PrepareFile import size
import PrepareFile

from PrepareFile import score_levels

# global variables
sim_caculator = PrepareFile.sim_caculator


# global variables
file_path = '/Users/yongqi/PycharmProjects/RiskAssessment/inputfile/expert/rf_analysis.csv'
risks = []

# class definition
# class riskDefinition(object):
def inputEval():
    '''
    读取rf_analysis.csv，获取到所有专家对风险的语言描述评级
    :return: 所有风险的每一个因素的专家评级： [风险名称,[prob1，prob2...],[impact1,impact2...]]
    '''
    with open(file_path,'r') as inputfile:
        riskEval = []
        for (index,line) in enumerate(inputfile):
            index = index+1
            if index & 1 == 1:
                #奇数行为风险因素名称
                riskEval = [line,[],[]]
            else:
                #偶数行为风险评级
                eval = line.split(',')
                for i in range(expert_count):
                    probability_eval = eval[i]
                    fn = init_fuzzy(probability_eval)
                    riskEval[1].append(fn)
                for j in range(expert_count,2*expert_count,1):
                    impact_eval = eval[j]
                    fn = init_fuzzy(impact_eval)
                    riskEval[2].append(fn)
                risks.append(riskEval)
    return risks
# def getTotalEval():
#
#     totalRisk = []
#     eachRisk = []
#     for eachEval in risks:
#         print eachEval[1],eachEval[2]
#         eachRisk = [eachEval[0],[],[]]
#         # probability 聚合
#         eachRisk[1] = fuzzy_plus(eachEval[1])
#         # impact 聚合
#         eachRisk[2] = fuzzy_plus(eachEval[2])
#         totalRisk.append(eachRisk)
#     return totalRisk
#

def getTotalEval():
    totalRisk = []
    riskComment = []
    for eachEval in risks:
        for c in range(expert_count):
            # 聚合
            tmp = fuzzy_multiple(eachEval[1][c],eachEval[2][c])
            riskComment.append(tmp)
            print 'Comment',tmp
        multipleRes = fuzzy_plus(riskComment)
        # divRes = fuzzy_division(multipleRes,fuzzy_plus(eachEval[2]))
        divRes = fuzzy_division(multipleRes,fuzzy_plus(eachEval[1]))
        # divRes = multipleRes

        totalRisk.append([eachEval[0],divRes])
        riskComment = []
    return totalRisk


# function definition

# main function
if __name__ == '__main__':
    inputEval()

    # 这里获取到的totaoRes包括了所有类型风险的模糊风险值
    # [[风险1名称，风险1模糊值]，[风险2名称，风险2模糊值]，[风险3名称，风险3模糊值]，......]

    totalRes = getTotalEval()
    print totalRes
    for i in totalRes:
        # print i[0]
        sims1 = []
        target_fn = FuzzyNumber.fnWithHeight(i[1], 1)
        for key in score_levels.keys():
            # 计算当前风险和所有等级的相似度
            level_fn = FuzzyNumber.fnWithHeight(score_levels[key], 1)
            # sims1.append([key, FuzzyNumber.simlarity_caculator7(target_fn, level_fn)])
            # sims1.append([key, FuzzyNumber.simlarity_caculator3(target_fn, level_fn)])
            # sims1.append([key, FuzzyNumber.simlarity_caculator4(target_fn, level_fn)])
            sims1.append([key, FuzzyNumber.simlarity_caculator9(target_fn, level_fn)])
            # sims1.append([key, FuzzyNumber.simlarity_caculator6(target_fn, level_fn)])

        max_sim1 = max(sims1, key=lambda sim1: sim1[1])
        sorted_sims1  = sorted(sims1, key=lambda sim1: sim1[1])
        risk_level1 = max_sim1[0]
        print i[0]+':'+risk_level1

        # risk_table = prettytable.PrettyTable([ '风险等级','Chen相似度'])
        # risk_table = prettytable.PrettyTable([ '风险等级','Xu相似度'])
        # risk_table = prettytable.PrettyTable([ '风险等级','Khorshidi相似度'])

        # risk_table = prettytable.PrettyTable([ '风险等级','Chutia相似度'])

        risk_table = prettytable.PrettyTable([ '风险等级','Chutia optimization相似度'])

        #  输出相似度
        risk_table.add_row(['-----------','--------'])
        for j in sorted_sims1:
            risk_table.add_row([j[0],j[1]])
        print(risk_table)


        # 以下是完整的
    # inputEval()
    # totalRes = getTotalEval()
    # risk_factors = []
    # for risk in totalRes:
    #     # print '风险名称：', risk[0]
    #     # print '发生概率：', risk[1]
    #     # print '产生影响：', risk[2]
    #     risk_factor = riskFactor(risk[0].strip(),risk[1],risk[2])
    #     # print risk_factor.risk_name,
    #     risk_factor.getRiskscore()
    #     risk_factors.append(risk_factor)
    # sorted_risks = sortRisk(risk_factors)
    # # risk_table = prettytable.PrettyTable(['风险名称','风险值'])
    # # risk_table.add_row(['-----------','---'])
    # # for i in sorted_risks:
    # #     print i.risk_name
    # #     risk_table.add_row([i.risk_name, i.risk_score])
    # # risk_table.border = 1
    #
    # # risk_table = prettytable.PrettyTable(['风险名称', '风险值','风险等级chen','Xu','Khorshidi','Chutia','Chutia optimization'])
    # risk_table = prettytable.PrettyTable(['风险名称', '风险值','风险等级Chutia optimization'])
    # risk_table.add_row(['-----------', '---','--------'])
    # for i in sorted_risks:
    #     print i.risk_name
    #     risk_table.add_row([i.risk_name, i.risk_score,i.risk_level1])
    # risk_table.border = 1
    # print(risk_table)
    # with open("/Users/yongqi/PycharmProjects/RiskAssessment/outfile/risk_assessment.csv", "w+") as similarity_out:
    #     similarity_out.write(str(risk_table))