
import os
print 'need a subdirectory ~/testindex'
print 'input file lookup.csv'


f=open('/Users/dc/TestCode/TestCoding/lookup.csv')
for line in iter(lambda: f.readline(), ''):
	#print line
	terms=line.split("|")
	print terms[0], terms[1]
	if os.path.exists("/Users/dc/TestCode/TestCoding/testindex/"+terms[1].strip()):
		fappend=open("/Users/dc/TestCode/TestCoding/testindex/"+terms[1].strip(),"a")
		fappend.write(terms[0]+"\n")
		fappend.close()
	else:
		fwrite=open("/Users/dc/TestCode/TestCoding/testindex/"+terms[1].strip(),"w")
		fwrite.write(terms[0]+"\n")
		fwrite.close()

f.close()
