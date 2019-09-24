|描述|路径|调用函数|参数|返回值名/格式|备注
|---|---|---|---|---|---|
|读取所有风险指标|/Users/yongqi/PycharmProjects/RiskAssessment/controlmodules/ReadConfig.py|readIndex()[0]|无|[str1,str2,str3...]||
|读取所有影响程度|/Users/yongqi/PycharmProjects/RiskAssessment/controlmodules/ReadConfig.py|readIndex()[1]|无|[str1,str2,str3...]||
|获取按照风险类别的分割区间|/Users/yongqi/PycharmProjects/RiskAssessment/controlmodules/ReadConfig.py|readIndex()[2]|无|[int1,int2,int3,int4]||
|获取四个类别各自风险等级|/Users/yongqi/PycharmProjects/RiskAssessment/sourcefile/newExcuteFile.py|compute_by_config(choice_arr)|[int1,int2,int3...]|out([str1,str2,str3,str4])||
|增加风险指标|/Users/yongqi/PycharmProjects/RiskAssessment/controlmodules/RiskManagement.py|index_management(category, name, impact, probability)|int,str,str,str,str|无|category可选1234，对应舆情、质量、效率、廉政|
|修改推送方式|/Users/yongqi/PycharmProjects/RiskAssessment/controlmodules/RiskManagement.py|send_management(level, isSend,receiver)|str,int,int|无|level可选为low、medium、high，isSend可选10对应是否，receiver可选012对应无、承办人员、承办人员&审管办|
|获取推送方式|/Users/yongqi/PycharmProjects/RiskAssessment/controlmodules/ReadConfig.py|readSend(level)|str|[str,str]|返回的isSend和receiver同上，不同数字对应不同策略，类型为字符串|
|风险预警推送|/Users/yongqi/PycharmProjects/RiskAssessment/controlmodules/RiskAlarm.py|riskAlarm(level)|str||在compute_risk_level后端函数中直接调用，直接映射到三个等级，根据config获取send的策略|
|发送推送消息|/Users/yongqi/PycharmProjects/RiskAssessment/controlmodules/RiskAlarm.py|sendAlarm(rcv)|[str,str]||从riskAlarm获取目标推送对象，进行消息推送，推送方式实现待补充|