#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : newExcuteFile.py
@Author: Grace
@Date  : 2019/4/9
@Desc  : 读取choice和impact，聚合风险要素，choice*impact计算模糊风险值
'''

# import modules
import PrepareFile
from FuzzyNumber import init_fuzzy
from FuzzyNumber import num_multiple_fuzzy
from FuzzyNumber import fuzzy_plus
from PrepareFile import stops
import FuzzyNumber
from PrepareFile import score_levels
from PrepareFile import Risk_names

# global variables
# 制定各类型风险有多少个要素
risk1 = PrepareFile.Risk1
risk2 = PrepareFile.Risk2
risk3 = PrepareFile.Risk3
risk4 = PrepareFile.Risk4
risk_count = len(stops)




impact_path = '/Users/yongqi/PycharmProjects/RiskAssessment/inputfile/expert/Impact_of_factors'
choice_path = '/Users/yongqi/PycharmProjects/RiskAssessment/inputfile/expert/Choice_of_factors'
# class definition

# function definition
def plus_separately(fn,stoplist):
    '''
    :param fn:
    :param stoplist:
    :return: list，包含了所有类型风险的模糊风险值
    给出所有风险要素的模糊数列表，指定stop，即各个类型风险有多少个要素
    stoplist长度和每个类型要素个数分配可变
    '''
    res = []
    tmp = 0
    for cc in stoplist:
        res.append(fuzzy_plus(fn[tmp:cc]))
        tmp = cc
    return res

impact_arr = ["very low", "low", "low", "low", "high", "high", "high", "fairly low", "high", "absolutely low", "fairly high", "fairly low", "fairly low"]





def compute_risk_level(choice_arr):
    f = []
    out = []
    totalRes = []
    for counter in range(len(choice_arr)):
        impact_fn = init_fuzzy(impact_arr[counter])
        fn_element = num_multiple_fuzzy(choice_arr[counter], impact_fn)
        f.append(fn_element)
        fns_of_risks = plus_separately(f,stops)
        # 这里获取到的totalRes只有所有风险的模糊风险值，按顺序存放，没有风险名称
        totalRes = fns_of_risks

    # 依次计算每一类风险的风险等级
    # for index, totalRes in enumerate(fns_of_risks):
    for index, i in enumerate(totalRes):

        # print i[0]
        sims1 = []
        target_fn = FuzzyNumber.fnWithHeight(i, 1)
        for key in score_levels.keys():
            # 计算当前风险和所有等级的相似度
            level_fn = FuzzyNumber.fnWithHeight(score_levels[key], 1)
            sims1.append([key, FuzzyNumber.simlarity_caculator9(target_fn, level_fn)])

        # 获取最高相似度
        max_sim1 = max(sims1, key=lambda sim1: sim1[1])
        sorted_sims1 = sorted(sims1, key=lambda sim1: sim1[1])

        # 最高相似度对应的级别
        risk_level1 = max_sim1[0]
        # print index+1,Risk_names[index]

        # y.append 传给前端[[x1,x2,x3...],[y1,y2,y3...]] x为风险类型，是固定的

        out.append(risk_level1)
    return out

        # alarm_levels = ['fairly high','high','very high','absolutely high']
        # if risk_level1 in alarm_levels:
        #     # 生成风险报告
        #     with open('')


def test():
    # 依次读取choice和impact
    counter = 1
    f = []
    out = []
    with open(impact_path,'r') as impact_file, open(choice_path,'r') as choice_file:
        for impact,choice in zip(impact_file,choice_file):
            counter = counter + 1
            impact_fn = init_fuzzy(impact)
            fn_element = num_multiple_fuzzy(choice,impact_fn)
            f.append(fn_element)
        fns_of_risks = plus_separately(f,stops)
        # 这里获取到的totalRes只有所有风险的模糊风险值，按顺序存放，没有风险名称
        totalRes = fns_of_risks

    # 依次计算每一类风险的风险等级
    # for index, totalRes in enumerate(fns_of_risks):
    for (index, i) in enumerate(totalRes):
        # print i[0]
        sims1 = []
        target_fn = FuzzyNumber.fnWithHeight(i, 1)
        for key in score_levels.keys():
            # 计算当前风险和所有等级的相似度
            level_fn = FuzzyNumber.fnWithHeight(score_levels[key], 1)
            sims1.append([key, FuzzyNumber.simlarity_caculator9(target_fn, level_fn)])

        # 获取最高相似度
        max_sim1 = max(sims1, key=lambda sim1: sim1[1])
        sorted_sims1 = sorted(sims1, key=lambda sim1: sim1[1])

        # 最高相似度对应的级别
        risk_level1 = max_sim1[0]
        print index+1,Risk_names[index]

        # y.append 传给前端[[x1,x2,x3...],[y1,y2,y3...]] x为风险类型，是固定的
        print risk_level1
        out.append(risk_level1)

    return out

        # alarm_levels = ['fairly high','high','very high','absolutely high']
        # if risk_level1 in alarm_levels:
        #     # 生成风险报告
        #     with open('')


# main function
if __name__ == '__main__':
    test()
