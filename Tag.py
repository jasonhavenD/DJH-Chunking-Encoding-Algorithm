#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:main
   Author:jason
   date:2018/3/15
-------------------------------------------------
   Change Activity:2018/3/15:
-------------------------------------------------
"""
import os
import sys
from optparse import OptionParser
from IO import tag as iotag
from BIO import tag as biotag
from BMEWO import tag as bmewotag
from BMEWOPlus import tag as bmewoplustag

# python Tag.py -t bio -i D:\github\A_DJH\DJH-Chunking-Encoding-Algorithm\corpus_pretreated.txt -o output.txt
if __name__ == '__main__':
	usage = "usage: python Tag.py -t[type] -i[input] [-o output]"
	parser = OptionParser(usage=usage)
	parser.add_option("-t", "--type", dest="type", metavar='type',
	                  help="choose a type of tag system")
	parser.add_option("-i", "--input", dest="input", metavar='input',
	                  help="choose a input file")
	parser.add_option("-o", "--out", dest="output", metavar='output',
	                  help="choose a output file")
	parser.add_option("-n", "--num", dest="coll_nums", metavar='coll_nums',
	                  help="set the nums of collumn")
	options, args = parser.parse_args()
	if options.type == None or options.input == None:
		print(usage)
		sys.exit(0)
	else:
		input = options.input
		output = options.output if options.output != None else 'output.txt'
		types = ['io', 'bio', 'bmewo', 'bmewoplus']
		if not os.path.exists(input):
			print('input file not exists!')
			sys.exit(0)
		if options.type not in types:
			print("illeagal tag's type!available types : ", types)
			sys.exit(0)
		if 'io' == options.type.lower():
			iotag.tag(input, output, coll_nums=options.coll_nums)
		elif 'bio' == options.type.lower():
			biotag.tag(input, output, coll_nums=options.coll_nums)
		elif 'bmewo' == options.type.lower():
			bmewotag.tag(input, output, coll_nums=options.coll_nums)
		else:
			bmewoplustag.tag(input, output, coll_nums=options.coll_nums)
