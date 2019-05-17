#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@File  : PrepareFile.py
@Author: Grace
@Date  : 2018/11/8
@Desc  : 如果有其他准备变量，保留该文件，如果全部都是模糊数建立的过程，删除直接调用EstablishFuzzy
'''

# import modules
import EstablishFuzzy
from decimal import Decimal
# global variables
'''
隶属度函数形式
'''
size = 4

'''
1：risk = probability*impact
'''
inference = 1
'''
专家人数
'''
expert_count = 8
'''
是否计算相似性
'''
sim_caculator = 1

# 用于newExcuteFile
# 制定每一类型风险各有多少个要素，可以从外面传
Risk_count = 4
Risk1 = 3
Risk2 = 3
Risk3 = 3
Risk4 = 3
first_stop = Risk1
second_stop = Risk1+Risk2
third_stop = second_stop + Risk3
forth_stop = third_stop + Risk4
stops = [first_stop, second_stop, third_stop, forth_stop]

Risk_names = ['舆情风险','质量风险','效率风险','廉政风险']
#############################################
# '''
# probability fuzzy numbers
# '''
# fuzzy_high = [0.7,0.9,1,1]
# fuzzy_medium = [0.2,0.5,0.5,0.8]
# fuzzy_low = [0,0,0.1,0.2]
# '''
# impact fuzzy numbers
# '''
# fuzzy_critical = [0.8,0.9,1,1]
# fuzzy_serious = [0.6,0.75,0.75,0.9]
# fuzzy_moderate = [0.3,0.5,0.5,0.7]
# fuzzy_minor = [0.1,0.25,0.25,0.4]
# fuzzy_negligible = [0,0,0.1,0.2]
# zero_backup = [0,0,0,0]



# ling_to_fuzzy = {'high':fuzzy_high,'medium':fuzzy_medium,'low':fuzzy_low,
#                        'critical':fuzzy_critical,'serious':fuzzy_serious,'moderate':fuzzy_moderate,
#                        'minor':fuzzy_minor,'negligible':fuzzy_negligible}

# 根据以下分级模糊数计算相似性
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
alow = [0, 0, 0, 0]
vlow = [0, 0, 0.02, 0.07]
low = [0.04, 0.1, 0.18, 0.23]
flow = [0.17, 0.22, 0.36, 0.42]
medium = [0.32, 0.41, 0.58, 0.65]
fhigh = [0.58, 0.63, 0.80, 0.86]
high = [0.72, 0.78, 0.92, 0.97]
vhigh = [0.93, 0.98, 1.0, 1.0]
ahigh = [1.0, 1.0, 1.0, 1.0]


zero_backup = [0,0,0,0]

score_levels = {'absolutely low':alow,'very low':vlow,'low':low,'fairly low':flow,
                'medium':medium,'fairly high':fhigh,'high':high,'very high':vhigh,
                'absolutely high':ahigh}

ling_to_fuzzy = {'absolutely low':alow,'very low':vlow,'low':low,'fairly low':flow,
                'medium':medium,'fairly high':fhigh,'high':high,'very high':vhigh,
                'absolutely high':ahigh}


def linguistic_to_fuzzy(linguistic):
    linguistic = linguistic.lower().strip()
    if linguistic != '':
        return ling_to_fuzzy[linguistic]
    else:
        return zero_backup

def precision(raw_num, preci):
    if preci == 2:
        return float(Decimal(raw_num).quantize(Decimal('0.00')))
    if preci == 3:
        return float(Decimal(raw_num).quantize(Decimal('0.000')))

# class definition

# function definition

# main function
if __name__ == '__main__':
    pass
