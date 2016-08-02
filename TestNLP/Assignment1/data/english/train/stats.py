#!/bin/python


f = open('en-universal-train.conll')
for line in f:
	if len(line) > 1:
		s=line.split('\t')
		print "s:",s
		print "s[word,head,POS]:",(s[1].lower(), s[6])
	

