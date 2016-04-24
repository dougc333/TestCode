#!/usr/bin/env python

#tested, ./clean.py returns empty ClouderaManager except for Cloudera Management Service
#test using ./addSM.py then clean.py; repest


import argparse
import sys

from cm_api.api_client import ApiResource, ApiException
from cm_api.endpoints.clusters import delete_cluster
from cm_api.endpoints.cms import ClouderaManager
from cm_api.endpoints.services import ApiService, ApiServiceSetupInfo
from time import sleep

import socket

service_types_and_names = {
  "SOLR":"solr",
  "YARN":"yarn",
  "HIVE":"hive",
  "HDFS":"hdfs",
  "ZOOKEEPER":"zookeeper",
  "HBASE":"hbase",
  "IMPALA":"impala"
}

CM_HOST=socket.gethostname()
cm_port = 7180
host_list=[
      'r2341-d5-us31.dssd.com',
      'r2341-d5-us32.dssd.com',
      'r2341-d5-us33.dssd.com',
      'r2341-d5-us34.dssd.com'
]

cdh_version="CDH5"


def stop_and_remove_services(api):
  print("list clusters")
  for c in api.get_all_clusters():
    print "cluster name:" + c.name + " cluster version:"+c.version
    for s in c.get_all_services():
      print "service type:" + s.type + " service name:"+s.name
      s.stop().wait()     
      c.delete_service(s.name) 
    delete_cluster(api,c.name)   

def cm_args_parser():
  parser = argparse.ArgumentParser()
  rint 'using CM_HOST:%s' % CM_HOST
  parser.add_argument("--cm-host",default=CM_HOST, help="name of CM host")
  parser.add_argument("--cm-user", default="admin", help="name of CM user")
  parser.add_argument("--cm-password", default="admin", help="CM password")
  return parser


def clean_all(api):
  """
  """
  cm = api.get_cloudera_manager()
  stop_and_remove_services(api)
  cms = cm.get_service()
  print "cms:", cms
  cms.stop().wait()
  cm.delete_mgmt_service()




def clean_hdfs(api):
  """
  """
  
 

def main():
  parser = cm_args_parser()
  args = parser.parse_args()
  print "Connecting to CM on host " + args.cm_host + "... ",
  api = ApiResource(args.cm_host, 
      username=args.cm_user, password=args.cm_password)
  print "done."

  #clean_all(api)


if __name__ == '__main__':
  main()

