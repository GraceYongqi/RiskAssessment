#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : RiskFactor.py
@Author: Grace
@Date  : 2018/11/8
@Desc  : 
'''

# import modules
import PrepareFile
import Defuzzification
import FuzzyNumber
from PrepareFile import precision
from operator import itemgetter
from PrepareFile import score_levels

# global variables
fuzzy_size = PrepareFile.size
inference = PrepareFile.inference
sim_caculator = PrepareFile.sim_caculator

# class definition
class riskFactor(object):
    '''
    分析对象-风险因素
    每一个风险因素由linguistic term给出probability和impact
    对两者进行转换称为模糊数，完成模糊推理后再去模糊化得到精确风险度
    '''
    # father_node = None
    # probability = []
    # impact = []
    risk_name = None
    fuzzy_probability = []
    fuzzy_impact = []
    fuzzy_score = []
    risk_score = 0
    # 当计算相似性时才会计算等级
    if sim_caculator == 1:
        risk_level1 = 0
        risk_level2 = 0
    def __init__(self,name, probability,impact):
        # self.father_node = father_node
        self.risk_name = name
        self.fuzzy_probability = probability
        self.fuzzy_impact = impact
    # def setProbImp(self,prob,imp):
    #     self.probability = prob
    #     self.impact = imp
    # def setFuzzynum(self):
    #     self.fuzzy_probability = PrepareFile.linguistic_to_fuzzy[self.probability]
    #     self.fuzzy_impact = PrepareFile.linguistic_to_fuzzy[self.impact]
    def setFuzzyscore(self):
        '''
        根据inference确定模糊数的运算公式
        :return: None
        '''
        if inference==1:
            self.fuzzy_score = FuzzyNumber.fuzzy_multiple(self.fuzzy_probability,self.fuzzy_impact)
            # for i in range(fuzzy_size):
                # self.fuzzy_score.append(self.fuzzy_probability[i]*self.fuzzy_impact[i])
        if sim_caculator == 1:
            sims1 = []
            sims2 = []
            sims3 = []
            sims4 = []
            sims5 = []
            target_fn = FuzzyNumber.fnWithHeight(self.fuzzy_score,1)
            print score_levels.keys()
            for key in score_levels.keys():
                # 计算当前风险和所有等级的相似度
                level_fn = FuzzyNumber.fnWithHeight(score_levels[key],1)
                sims1.append([key, FuzzyNumber.simlarity_caculator5(target_fn, level_fn)])
                # sims2.append([key, FuzzyNumber.simlarity_caculator3(target_fn, level_fn)])
                # sims3.append([key, FuzzyNumber.simlarity_caculator4(target_fn, level_fn)])
# 多峰值务必放在最后
#                 sims4.append([key, FuzzyNumber.simlarity_caculator5(target_fn, level_fn)])
#                 sims5.append([key, FuzzyNumber.simlarity_caculator6(target_fn, level_fn)])
                # 选择相似度最高的等级
            max_sim1 = max(sims1,key = lambda sim1:sim1[1])
            # max_sim2 = max(sims2,key = lambda sim2:sim2[1])
            # max_sim3 = max(sims3,key = lambda sim3:sim3[1])
            # max_sim4 = max(sims4,key = lambda sim4:sim4[1])
            # max_sim5 = max(sims5,key = lambda sim5:sim5[1])
            self.risk_level1 = max_sim1[0]
            # self.risk_level2 = max_sim2[0]
            # self.risk_level3 = max_sim3[0]
            # self.risk_level4 = max_sim4[0]
            # self.risk_level5 = max_sim5[0]
            # return sims1


    def getRiskscore(self):
        '''
        模糊风险值去模糊化得到单值
        确定模糊数的实际模型
        :return: self.risk_score
        '''
        # self.setFuzzynum()
        self.setFuzzyscore()
        fuzzy = []
        for i in self.fuzzy_score:
            if i not in fuzzy:
                fuzzy.append(i)
        fuzzy_len = len(fuzzy)
        if fuzzy_len == 3:
            self.risk_score = Defuzzification.triangle_defuzzification(fuzzy)
        elif fuzzy_len == 4:
            self.risk_score = Defuzzification.trapezoidal_defuzzification(fuzzy)
        self.risk_score = precision(self.risk_score,3)
        return self.risk_score

def sortRisk(rfs):

    sortedRisks = sorted(rfs,key = lambda rf:rf.risk_score)
    # sortedRisks = sorted(rfs,key = )
    return sortedRisks

# main function
if __name__ == '__main__':
    pass
