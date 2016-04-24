#!/usr/bin/env python

#status: we can update the parameters in role config group for dssd datanode
#the role config groups are config for all 3 data nodes
#the role configs are for eacn datanode


import sys
import argparse
import subprocess
from cm_api.api_client import ApiResource
from cm_api.api_client import ApiException
from cm_api.endpoints.clusters import create_cluster
from cm_api.endpoints.clusters import delete_cluster
from cm_api.endpoints.cms import ClouderaManager
from cm_api.endpoints.parcels import get_parcel



from time import sleep
import re


def HDD_hdfs_config(api):
  cluster = api.get_cluster("HDDTest")
  hdfs_service = cluster.get_service("HDFS")
  hdfs_config = hdfs_service.get_config(view="Full")
  print "---------------------------hdfs_config------------------"
  print "HDD_hdfs_config:", hdfs_config
  print "-------------------------end_hdfs_config----------------"
  #HDD doesnt need anything configured here.. 
  return hdfs_service


def D5_hdfs_config(api):
  print "check hdfs config"
  cluster = api.get_cluster("d5Test")
  hdfs_service = cluster.get_service("HDFS")
  hdfs_config = hdfs_service.get_config(view="Full")
  print "---------------------------hdfs_config------------------"
  print "hdfs_config:", hdfs_config
  print "-------------------------end_hdfs_config----------------"
  hdfs_config= {
        "com_dssd_hadoop_floodds_usablecapacity": 100000000000000,
        "com_dssd_hadoop_floodds_volume": "twu_vol"
  }
  hdfs_service.update_config(hdfs_config)

  return hdfs_service
  
def config_dssd_datanode(hdfs_service):
  #dig into roles to find DN and NN configs
  # SCR in datanode config
  print "---------dssd_datanode_base_role_config_groups----------------------"
  dn_dssd_rcg = hdfs_service.get_role_config_group('HDFS-DSSDDATANODE-BASE')
  datanode_rcg_config = dn_dssd_rcg.get_config(view="Full")
  print "datanode_rcg_config:", datanode_rcg_config
  print "----------end_dssd_datanode_base_rcg--------------------------------" 
  rcg_config = {
         'dfs_datanode_max_xcievers': 4096,
         'dssddatanode_web_metric_collection_enabled': True,
         'dssddatanode_host_health_enabled': True, 
         'dfs_datanode_readahead_bytes': 1024*1024*1024*128,
         'com_dssd_flood_conn_qmax': 2,
         'com_dssd_flood_conn_client_qdepth':128,
         'com_dssd_flood_conn_cpus': '26,28,30'
   }
  dn_dssd_rcg.update_config(rcg_config)
  print "-----------dn_dssd_role_config_group_all_roles---------------------"
  print "roles in datanode role_config_group:", dn_dssd_rcg.get_all_roles()
  print "-----------end dn_dssd_role_config_group_all_roles-----------------"
  
  print "-----------------hdfs_role_config_groups--------------------------"
  print "hdfs_role_config_groups:",hdfs_service.get_all_role_config_groups()
  print "-----------------end_hdfs_role_config_groups----------------------"  

  
  print "-----------------hdfs_service_role_types---------------------------"
  print "hdfs_role_types:", hdfs_service.get_role_types()
  print "-----------------end_hdfs_service_role_types-----------------------"
  
  print "-----------------hdfs_roles----not needed. for each node-----------"
  print "hdfs_roles:",hdfs_service.get_all_roles(view="Full")
  print "-----------------end_hdfs_roles------------------------------------"



def cm_args_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument("--cm_host",default='r2341-d5-us01',help="url for host")
  parser.add_argument("--cm_user",default='admin', help='default user name')
  parser.add_argument("--cm_password",default='admin',help='default password for default user name')
  return parser


def main():
  parser = cm_args_parser()
  args = parser.parse_args()
  print "connecting to host:" + args.cm_host + "..."
  api = ApiResource(args.cm_host, username=args.cm_user, password=args.cm_password)
  print "done..."
  hdfs_service = hdfs_config(api)
  config_dssd_datanode(hdfs_service)


if __name__ == '__main__':
  main()
  
