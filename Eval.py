#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   测评
   File Name:eval.py
   Author:jason
   date:2018/3/15
-------------------------------------------------
   Change Activity:2018/3/15:
-------------------------------------------------
"""
import pandas
import codecs

'''
0. 正确率 accuracy  = 预测正确的某实体个数 /  预测样本所有
1. 精确率（查准率）precision = 预测为某实体的正确个数 /  预测为某实体的总数 #预测中有多少是正例
2. 召回率（查全率） = 预测为某实体的正确个数 /  训练样本中的某实体总数 #预测中正例覆盖系统中正例的多少
3.   F1值  = 正确率 * 召回率 * 2 / (正确率 + 召回率) （F 值即为正确率和召回率的调和平均值）


reference
https://www.zhihu.com/question/19645541
https://wenku.baidu.com/view/c7c205fa58fafab068dc0275.html



'''
delimiter = '\t'

if __name__ == '__main__':
	file = 'test/result.txt'
	text = []
	with codecs.open(file, 'r', encoding='utf-8') as f:
		for line in f.readlines():
			line = line.strip()
			if len(line.split()) == 4:
				text.append(line.split(delimiter))  # 根据语料修改
	
	df = pandas.DataFrame(text, columns=['character', 'postag', 'correct', 'predict'])
correct = df[df.correct == df.predict]
for i in ('O','I_TIME', 'I_NAME', 'I_LOCATION', 'I_ORGNIZATION', 'I_PROFESSION', 'I_NOUN'):
	if sum(df.predict == i) == 0 or sum(df.correct == i) == 0:  # 数据不涉及到该类别
		continue
	P = sum(correct.predict == i) / sum(df.predict == i)
	R = sum(correct.predict == i) / sum(df.correct == i)
	F1 = R * P * 2 / (R + P)
	print(i, '\t:\t', ' P=', P, 'R=', R, ' F1=', F1)
