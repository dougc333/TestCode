
import os
print 'need a subdirectory ~/testindex'
print 'input file lookup.csv'


f=open('/home/dc/lookup.csv')
for line in iter(lambda: f.readline(), ''):
	#print line
	terms=line.split("|")
	print terms[0], terms[1]
	if os.path.exists("/home/dc/testindex/"+terms[1].strip()):
		fappend=open("/home/dc/testindex/"+terms[1].strip(),"a")
		fappend.write(terms[0]+"\n")
		fappend.close()
	else:
		fwrite=open("/home/dc/testindex/"+terms[1].strip(),"w")
		fwrite.write(terms[0]+"\n")
		fwrite.close()

f.close()
