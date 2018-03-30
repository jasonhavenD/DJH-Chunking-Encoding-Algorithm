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

delimiter = '\t'


def read_tags():
	lst = []
	dic = {}
	with codecs.open('IO/entities_tag.csv', 'r', encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=' ')
		for row in reader:
			lst.append(row[1])
			dic[row[1]] = row[2]
	return lst, dic


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
	postags, tagdic = read_tags()
	
	result_text = []
	for line in text:
		if '' != line.strip():
			# word, tag = line.split(delimiter)
			temps = line.split(delimiter)
			tag = temps[coll_nums - 1]
			if tag.strip() in postags:
				line = line.replace('\n', '') + delimiter + tagdic[tag.strip()] + '\n'
			else:
				line = line.replace('\n', '') + delimiter + 'O' + '\n'
		result_text.append(line)
	# save
	save_data(result_text, output)
	end = datetime.datetime.now()
	print('finished in ' + str((end - begin).seconds) + ' s!')
