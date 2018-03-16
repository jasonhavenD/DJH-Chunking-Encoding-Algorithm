#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   功能：分词并做词性标注
   File Name:Pos_tag
   Author:jason
   date:2018/3/16
-------------------------------------------------
   Change Activity:2018/3/16:
-------------------------------------------------
"""
from stanfordcorenlp import StanfordCoreNLP

if __name__ == '__main__':
	corenlp = StanfordCoreNLP()
	print(corenlp.ner('你好'))
