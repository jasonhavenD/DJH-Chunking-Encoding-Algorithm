#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:peopledaily
   Author:jason
   date:2018/3/15
-------------------------------------------------
   Change Activity:2018/3/15:
-------------------------------------------------
"""
import re


class PeopleDailyUtil():
	__delimiter = None
	__tokens = None
	__line = None
	
	def __init__(self, delimiter, line):
		self.__delimiter = delimiter
		self.__line = line
		self.__tokens = line.split(delimiter)
	
	def merge_time(self):
		# 时间合并，有待优化
		regex = re.compile(
			"\d{2,4}年/t|[零一二三四五六七八九十]{2,4}年/t|\d{1,2}月/t|[一二三四五六七八九十]{1,2}月/t|\d{1,3}日/t|[一二三四五六七八九十]{1,3}日/t|\d{1,2}时/t|[零一二三四五六七八九十]{1,3}时/t|\d{1,3}分/t|[零一二三四五六七八九十]{1,3}分/t|\d{1,3}秒/t|[零一二三四五六七八九十]{1,3}秒/t|[零一二三四五六七八九十]{1,3}点/t")
		
		# 分时间块
		groups = []
		first_index = -1
		last_index = -1
		i = 0
		j = 0
		while i < len(self.__tokens):
			t = self.__tokens[i]
			if regex.match(t):
				if first_index == -1:  # 找到块的第一个时间
					first_index = i
					j = 0
					while j < len(self.__tokens[i + 1:]):
						tt = self.__tokens[i + 1 + j]
						# if regex.match(tt) or ''==tt.strip():#解决相邻时间有多个空格的时候无法将相邻时间分在一个块的问题，其实是语料本身的问题
						if regex.match(tt):
							last_index = i + 1 + j  # 找到块的最后一个时间
							j += 1
						else:
							last_index = i + j  # 找到块的最后一个时间
							break
					# print(first_index, last_index, self.__tokens[first_index:last_index + 1])
					groups.append((first_index, last_index))
					i = last_index
					first_index = -1
					last_index = -1
			i += 1
		
		# 合并每个时间块
		merges = []
		for i, g in enumerate(groups):
			a, b = g
			time_tokens = self.__tokens[a:b + 1]
			merge = ''
			for t in time_tokens:
				merge += t[:t.index('/t')]
			merge += '/t'
			merges.append(merge)
		# print(merges)
		
		# 更新
		merges.reverse()
		for i, g in enumerate(groups[::-1]):
			a, b = g
			self.__tokens[a:b + 1] = [merges[i]]
	
	def merge_name(self):
		# 姓名合并
		regex = re.compile('.+/nr')
		
		# 名字分块
		groups = []
		first_index = -1
		last_index = -1
		i = 0
		j = 0
		while i < len(self.__tokens):
			t = self.__tokens[i]
			if regex.match(t):
				if first_index == -1:  # 找到块的第一个
					first_index = i
					j = 0
					while j < len(self.__tokens[i + 1:]):
						tt = self.__tokens[i + 1 + j]
						if regex.match(tt):
							last_index = i + 1 + j  # 找到块的最后一个
							j += 1
						else:
							last_index = i + j  # 找到块的最后一个
							break
					# print(first_index, last_index, self.__tokens[first_index:last_index + 1])
					groups.append((first_index, last_index))
					if last_index == -1:
						break
					i = last_index
					first_index = -1
					last_index = -1
			i += 1
		# 合并名字
		merges = []
		for i, g in enumerate(groups):
			a, b = g
			name_tokens = self.__tokens[a:b + 1]
			merge = ''
			for t in name_tokens:
				merge += t[:t.index('/nr')]
			merge += '/nr'
			merges.append(merge)
		# print(merges)
		
		# 更新
		merges.reverse()
		for i, g in enumerate(groups[::-1]):
			a, b = g
			self.__tokens[a:b + 1] = [merges[i]]
		return self.__tokens
	
	def merge_brackets(self):
		# 括号内部合并
		content_regex = re.compile('\[((.+?)/(.+?))\]')
		tag_regex = re.compile('\](\w+)')
		contents = re.findall(content_regex, self.__line)
		tags = re.findall(tag_regex, self.__line)
		
		# 确定块的位置
		groups = []
		first_index = -1
		last_index = -1
		i = 0
		j = 0
		while i < len(self.__tokens):
			t = self.__tokens[i]
			if first_index == -1 and t != '' and '[' == t[0]:  # 找到块的第一个
				first_index = i
			if first_index != -1 and t.count(']') != 0:
				last_index = i
				# print(first_index, last_index, self.__tokens[first_index:last_index + 1])
				groups.append((first_index, last_index))
				i = last_index
				first_index = -1
			i += 1
		
		# 合并
		# print(contents)
		merges = []
		for content in contents:
			merge = ''
			for t in content[0].split(self.__delimiter):
				merge += t[:t.index('/')]
			merges.append(merge)
		for i in range(len(merges)):
			merges[i] = merges[i] + '/' + tags[i]
		# print(merges)
		
		# 更新
		merges.reverse()
		for i, g in enumerate(groups[::-1]):
			a, b = g
			self.__tokens[a:b + 1] = [merges[i]]
	
	@property
	def delimiter(self):
		return self.__delimiter
	
	@property
	def line(self):
		return self.__line
	
	@property
	def tokens(self):
		return self.__tokens
