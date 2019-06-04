# RiskAssessment
注意！！！
应用层代码（ExcuteFile和newExcuteFile）里用到的模糊数都是权值只有一个，且为1
FuzzyNumber里所有运算函数都只适用于应用层的权值为1的模糊数，因为运算函数里没有涉及权值，
是在应用层聚合完成后，在计算相似度之前append了末尾的权值为1

算法比较中直接用数组形式初始化fnwithheight，不涉及运算，直接比较相似度


算法比较：
similaritycalculators python main.py

计算流程风险级别：
sourcefile python InputFile.py

expert/rf_analysis.csv
A1 #风险因素名称
very low,very low,high,very low,low,fairly low,fairly low,high,absolutely low,fairly high,fairly low,fairly low,fairly low,very low,low,fairly high

设定好专家人数 expert_count = 8
前面8个probability，后面8个impact

python InputFile\.py 是读取rf_analysis.csv中的8位专家的评价短语计算风险值
涉及到聚合算法

python newExcuteFile\.py 是连到前端的后台模型，前端传递1/0选项，后端直接用1/0做系数得到乘积之和
不涉及聚合算法，是当前的审判风险模型
