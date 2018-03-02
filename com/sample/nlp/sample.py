# -*- coding: utf-8 -*-
# encoding=utf-8

import jieba
import jieba.analyse
import urllib2
from HTMLParser import HTMLParser
import re

req = urllib2.Request("https://zhuanlan.zhihu.com/p/30354720")
response = urllib2.urlopen(req)
html = response.read()
# print html

class MyParser(HTMLParser):
    def __init__(self):
        self.txt = ""
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        # print "Encountered a start tag:", tag, attrs
        pass

    def handle_endtag(self, tag):
        # print "Encountered an end tag :", tag
        pass

    def handle_data(self, data):
        self.txt += data.strip()
        print "Encountered some data  :", data


parser = MyParser()
parser.feed(html)
print parser.txt

sentence = parser.txt
tags = jieba.analyse.extract_tags(sentence, 10)
print tags

words = jieba.cut(sentence, cut_all=False)
print "|".join(words)

# tags2 = jieba.analyse.textrank(sentence, 10)
# print tags2
