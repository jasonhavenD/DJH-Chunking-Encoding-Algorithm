#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:io
   Author:jason
   date:2018/3/15
-------------------------------------------------
   Change Activity:2018/3/15:
-------------------------------------------------
"""
import codecs


class IOUtil():
	@staticmethod
	def load_files(files):
		'''
		:param files:文件列表
		:return:文件内容
		'''
		text = []
		print(files)
		for file in files:
			if file:
				with codecs.open(file, 'rb', encoding='utf-8') as f:
					text.extend(f.readlines())
		return text
	
	@staticmethod
	def save_to_file(result_text, save_file):
		# 保存到文件
		with codecs.open(save_file, 'w', encoding='utf-8') as f:
			for line in result_text:
				for token in line:
					f.write(token.replace('/', ' ') + '\n')
				f.write('\n')
