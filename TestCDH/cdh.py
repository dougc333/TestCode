#!/usr/bin/env python

import argparse
import sys

from cm_api.api_client import ApiResource
from cm_api.api_client import ApiException
from cm_api.endpoints.clusters import create_cluster
from cm_api.endpoints.clusters import delete_cluster
from cm_api.endpoints.cms import ClouderaManager
from cm_api.endpoints.services import ApiService, ApiServiceSetupInfo
from time import sleep

service_types_and_names = {
  "SOLR":"solr",
  "YARN":"yarn",
  "HIVE":"hive",
  "HDFS":"hdfs",
  "ZOOKEEPER":"zookeeper",
  "HBASE":"hbase",
  "IMPALA":"impala"
}

cm_host="r2341-d5-us01"
cm_port = 7180
host_list=[
      'r2341-d5-us01.dssd.com',
      'r2341-d5-us02.dssd.com',
      'r2341-d5-us03.dssd.com',
      'r2341-d5-us04.dssd.com'
]
cdh_version="CDH5"


def stop_services(api):
  print("list clusters")
  for c in api.get_all_clusters():
    print "cluster name:" + c.name + " cluster version:"+c.version
    for s in c.get_all_services():
      print "service type:" + s.type + " service name:"+s.name
      s.stop().wait()     
      c.delete_service(s.name) 
    
 
def change_dssd():
  cm.update_config({"dssd_enabled": True})

def cm_args_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument("--cm-host", help="name of CM host")
  parser.add_argument("--cm-user", default="admin", help="name of CM user")
  parser.add_argument("--cm-password", default="admin", help="CM password")
  return parser

#our scenario is different; we assume cloudera-agent is running on all the hosts so the 
#hosts will be part of the cm; lets see if we can first list the existing hosts 
def startHDD(api):
  cluster = create_cluster(api, "HDDCluster", "CDH5")
  #cluster = api.get_cluster("HDDCluster")
  cluster.add_hosts(host_list)
  #service_setup = ApiServiceSetupInfo(name="mgmt", type="MGMT")
  cm=api.get_cloudera_manager()
  #cm.create_mgmt_service(service_setup)
  #cmd = cm.host_install("root", host_list, password="888avb888", cm_repo_url=None) 
  #print "Installing hosts. This might take a while."
  #while cmd.success == None:
  #  sleep(5)
  #  cmd = cmd.fetch()

  #if cmd.success != True:
  #  print "cm_host_install failed: " + cmd.resultMessage
  #  exit(0)

  #print "cm_host_install succeeded"
  #for addMe in service_types_and_names:
  #  print "addMe:" + addMe
  #  print "addMe[addMe]:" + service_types_and_names[addMe]
  #  service = cluster.create_service(addMe,service_types_and_names[addMe])
  

def main():
  parser = cm_args_parser()
  args = parser.parse_args()

  print "Connecting to CM on host " + args.cm_host + "... ",
  api = ApiResource(args.cm_host, 
      username=args.cm_user, password=args.cm_password)
  print "done."

  #cm = api.get_cloudera_manager()
  #stop_services(api)
  #//delete_cluster(api, "cluster")
  #cm.update_config({"dssd_enabled": False})
  startHDD(api)

if __name__ == '__main__':
  main()

