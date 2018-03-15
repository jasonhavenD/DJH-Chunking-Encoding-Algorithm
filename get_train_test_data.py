#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:get_train_test_data
   Author:jason
   date:2018/3/15
-------------------------------------------------
   Change Activity:2018/3/15:
-------------------------------------------------
"""
import codecs

if __name__ == '__main__':
	input = 'output.txt'
	train = 'train.txt'
	test = 'test.txt'
	text = []
	with codecs.open(input, 'r', encoding='utf-8') as f:
		text = f.readlines()
	with codecs.open(train, 'w', encoding='utf-8') as f:
		for line in (text[:int(len(text) * 0.7)]):
			f.write(line)
	with codecs.open(test, 'w', encoding='utf-8') as f:
		for line in (text[:int(len(text) * 0.3)]):
			f.write(line)
