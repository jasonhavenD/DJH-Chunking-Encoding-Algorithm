#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:bakeoff2005
   Author:jason
   date:2018/3/16
-------------------------------------------------
   Change Activity:2018/3/16:
-------------------------------------------------
"""
import codecs


class Bakeoff2005Util():
	def pos_tag_for_crf(self, input_data, output_file):
		# result_data = []
		output_data = codecs.open(output_file, 'w', 'utf-8')
		for line in input_data:
			word_list = line.strip().split()
			for word in word_list:
				if len(word) == 1:
					output_data.write(word + "\tS\n")
				# result_data.append(word + "\tS\n")
				else:
					output_data.write(word[0] + "\tB\n")
					# result_data.append(word[0] + "\tB\n")
					for w in word[1:len(word) - 1]:
						output_data.write(w + "\tM\n")
					# result_data.append(w + "\tM\n")
					output_data.write(word[len(word) - 1] + "\tE\n")
				# result_data.append(word[len(word) - 1] + "\tE\n")
			output_data.write("\n")
		# result_data.append('\n')
		output_data.close()
