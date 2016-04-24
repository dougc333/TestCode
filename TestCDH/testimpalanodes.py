
#!/usr/bin/python


import os
import socket
import re
import urllib


listDaemons=['r2341-d5-us02' , 'r2341-d5-us03' , 'r2341-d5-us04'];
for a in listDaemons:
  content = urllib.urlopen("http://r2341-d5-us02:25000/varz?raw".format(a)).read()
  mem_limit_gb = float(re.findall('--mem_limit=(\d+)', content)[0])/(1024**3)
  print mem_limit_gb



