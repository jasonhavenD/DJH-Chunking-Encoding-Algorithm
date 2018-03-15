#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:tag
   Author:jason
   date:2018/3/15
-------------------------------------------------
   Change Activity:2018/3/15:
-------------------------------------------------
"""
import datetime
import os
import codecs
import csv

delimiter = ' '


def read_tags():
	lst = []
	with codecs.open('BIO/entities_tag.csv', 'r', encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=' ')
		for row in reader:
			lst.append(row[1])
	return lst


def load_data(input):
	with codecs.open(input, 'r', encoding='utf-8') as f:
		return f.readlines()


def save_data(text, output):
	path = os.getcwd() + '/' + output
	with codecs.open(output, 'w', encoding='utf-8') as f:
		for line in text:
			f.write(line)
	print('save output as' + path)


def tag(input, output, coll_nums=2):
	print('start to tag...')
	begin = datetime.datetime.now()
	# load
	text = load_data(input)
	# main
	# 读取实体标记规则文件entities_tag
	entities_tags = read_tags()
	print(entities_tags)
	
	result_text = []
	for line in text:
		if '' != line.strip():
			word, tag = line.split(delimiter)
			if tag.strip() in entities_tags:
				line = line.replace('\n', '') + delimiter + 'A' + '\n'
		result_text.append(line)
	# save
	save_data(result_text, output)
	end = datetime.datetime.now()
	print('finished in ' + str((end - begin).seconds) + ' s!')
