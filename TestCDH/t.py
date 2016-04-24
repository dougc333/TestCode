#!/usr/bin/env python

CM_HOST='r2341-d5-us01'
CM_USER='admin'
CM_PASS='admin'
CM_USE_TLS=False

import sys
from cm_api.api_client import ApiResource

class t(object):
 """
 """
 def __init__(self):
   self.api=ApiResource(CM_HOST, username=CM_USER, password=CM_PASS,use_tls=CM_USE_TLS)
 def processQuery(query):
   print "processing %s" % query

def main(argv):
  print "main"
  t1 = t()
  t.processQuery("select cpu_percent")

if __name__=='__main__':
  sys.exit(main(sys.argv))

