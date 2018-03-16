#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   功能：标签语料之前对数据预处理
   要求待处理数据：词性标注后的数据
   格式：
   token<space>postag
   token<space>postag
   或
   token<tab>postag
   token<tab>postag
-------------------------------------------------
   File Name:Corpus_Pretreatment
   Author:jason
   date:2018/3/14
-------------------------------------------------
   Change Activity:2018/3/14:
-------------------------------------------------
"""

import os
import sys
import datetime
from optparse import OptionParser
from util.peopledaily import PeopleDailyUtil
from util.io import IOUtil


def peopledaily(files, save_file):
	'''
	人民日报语料库预处理
	:param files:
	:param save_file:
	:return:
	'''
	text = IOUtil.load_files(files)
	
	begin = datetime.datetime.now()
	print('start to pretreat...')
	
	result_text = []
	
	for line in text:
		# tokens = line.split(delimiter)  # 根据语料处理，空格个数、tab等等
		# print(tokens)
		peopledaily = PeopleDailyUtil(delimiter='  ', line=line)
		
		#  时间合并，有待优化
		peopledaily.merge_time()
		# print('时间合并完成')
		# 括号内部合并
		peopledaily.merge_brackets()
		# print('括号内部合并完成')
		# 姓名合并
		peopledaily.merge_name()
		# print('姓名合并完成')
		result_text.append(peopledaily.tokens)
	
	# /变空格或者TAB,保存到文件
	IOUtil.save_to_file(result_text, save_file)
	end = datetime.datetime.now()
	print('finished in ' + str((end - begin).seconds) + ' s!')
	print('save as ' + save_file)


def diy_treat(files, save_file):
	'''
	:param files:
	:param save_file:
	:return:
	'''
	print("diy test file")


def pre_treat(source_file, save_file, default=True):
	'''
	:param corpus:预处理的数据
	:param save_file:保存的文件
	:param default:是否使用默认数据
	:return:
	'''
	if default:
		dir = os.getcwd() + '/corpora/' + source_file + '/data/'
		files = os.listdir(dir)
		eval(source_file)([dir + f for f in files], save_file)  # 动态调用
	else:
		file = source_file
		dir = os.getcwd()
		diy_treat([dir + file], save_file)


# 获取当前可用的语料
def get_available_corpora():
	corpora = []
	dir = os.getcwd() + '/corpora/'
	for f in os.listdir(dir):
		corpora.append(str(f))
	return corpora


# python Corpus_Pretreatment.py -c peopledaily
if __name__ == '__main__':
	usage = "usage: python Corpus_Pretreatment.py [[-c|--corpus]|[-f|--file]] [-s|--save]"
	parser = OptionParser(usage=usage)
	available_corpora = get_available_corpora()
	corpora_help = str([name for name in available_corpora])
	parser.add_option("-c", "--corpus", dest="corpus", metavar='corpus',
	                  help="choose which corpus to process:" + corpora_help)
	parser.add_option("-f", "--file", dest="source", metavar='source',
	                  help="choose a source file to pretreat")
	parser.add_option("-s", "--save", dest="save_file", metavar='save_file', default='corpus_pretreated.txt',
	                  help="save corpus pretreated to disk")
	options, args = parser.parse_args()
	if options.corpus == None:
		print(usage)
		sys.exit(0)
		pass
	else:
		if options.corpus not in available_corpora:
			print("available_corpora:", available_corpora)
			sys.exit(0)
		else:
			if options.source:  # 优先用户自定义的数据
				pre_treat(options.source, options.save_file, default=False)
			else:
				pre_treat(options.corpus, options.save_file)
