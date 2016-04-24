#!/usr/bin/env python

import sys
import urllib2
import requests
import json


impalad_nodes=['http://r2341-d5-us02:25000','http://r2341-d5-us03:25000','http://r2341-d5-us04:25000']
jmx_nodes=['http://r2341-d5-us02:50075/jmx?qry=Hadoop:service=DataNode,name=DataNodeActivity-r2341-d5-us02.dssd.com-50010',
           'http://r2341-d5-us03:50075/jmx?qry=Hadoop:service=DataNode,name=DataNodeActivity-r2341-d5-us03.dssd.com-50010',
           'http://r2341-d5-us04:50075/jmx?qry=Hadoop:service=DataNode,name=DataNodeActivity-r2341-d5-us04.dssd.com-50010']

def main():
  print "testing jmx and metric capture"
  for hosts in impalad_nodes:
     print "------------------------getting impalad from %s-------------", hosts
     res = requests.get(hosts)
     print res.text
     
  for hosts in jmx_nodes:
     print '-------------------------------------------------------------'
     req = urllib2.Request(hosts)
     opener=urllib2.build_opener()
     stream = opener.open(req)
     print json.load(stream)


if __name__=='__main__':
  main()
