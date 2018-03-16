#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   生成训练数据和测试数据
   File Name:get_train_test_data
   Author:jason
   date:2018/3/15
-------------------------------------------------
   Change Activity:2018/3/15:
-------------------------------------------------
"""
import codecs
import random
import numpy as np

if __name__ == '__main__':
	input = 'ne_chunked.txt'
	ftrain = 'test/train.txt'
	ftest = 'test/test.txt'
	text = []
	with codecs.open(input, 'r', encoding='utf-8') as f:
		text = f.readlines()
	
	train_index = random.sample(range(len(text)), int(len(text) * 0.008))
	test_index = random.sample(range(len(text)), int(len(text) * 0.002))
	
	train = np.array(text)[train_index]
	test = np.array(text)[test_index]
	
	with codecs.open(ftrain, 'w', encoding='utf-8') as f:
		for line in train:
			f.write(line)
	with codecs.open(ftest, 'w', encoding='utf-8') as f:
		for line in test:
			f.write(line)
