#!/usr/bin/env python

#debug hdfs setup, download rcgs
#install hdfs (nondssd and print out)
# install datanode and print

from cm_api.api_client import ApiResource
from cm_api.endpoints.clusters import ApiCluster
from cm_api.endpoints.clusters import create_cluster
from cm_api.endpoints.parcels import ApiParcel
from cm_api.endpoints.parcels import get_parcel
from cm_api.endpoints.cms import ClouderaManager
from cm_api.endpoints.services import ApiService, ApiServiceSetupInfo
from cm_api.endpoints.services import create_service
from cm_api.endpoints.types import ApiCommand, ApiRoleConfigGroupRef
from cm_api.endpoints.role_config_groups import get_role_config_group
from cm_api.endpoints.role_config_groups import ApiRoleConfigGroup
from cm_api.endpoints.roles import ApiRole
from time import sleep

import re

import argparse


lookfor=[ u'dfs_namenode_name_dir',
          u'dfs_name_dir',
          u'dfs_https_port',
          u'fs_defaultFS', 
          u'fs_default_name',
          u'dfs_namenode_acls_enabled',
          u'io_compression_codecs',
          u'dfs_blocksize',
          u'fs_permissions_umask-mode',
          u'dfs_datanode_hdfs-blocks-metadata_enabled',
          u'dfs_datanode_du_reserved', 
          u'dfs_client_domain_socket_data_traffic', 
          u'hadoop_rpc_protection',
          u'hadoop_security_authentication',
          u'hadoop_security_authorization',
          u'hadoop_ssl_require_client.cert',
          u'dfs_https_address',
          u'dfs_client_read_shortcircuit',
          u'dfs_client_read_shortcircuit_skip_checksum',
          u'dfs_client_domain_socket_data_traffic',
          u'dfs_client_use_legacy_blockreader',
          u'dfs_client_use_datanode_hostname'
         ]


def search(config_dict):
   for findMe in lookfor:
     print "looking for:", findMe
     if findMe in config_dict:
       print '----------------------------------'
       print 'found findMe', findMe
       print '----------------------------------'


def get_info(api):
  clusterList = api.get_all_clusters(view="Full")
  print "clusterList:%s", clusterList
  for cluster in clusterList:
    print "cluster: %s",cluster
    cm = api.get_cloudera_manager()
    print "cm config:",cm.get_config(view="Full")
    #search(cm.get_config(view="Full"))
    #exit(0)
    all_services = cluster.get_all_services(view="Full")
    #print "all_services:", all_services
    for service in all_services:
      print "service:", service
      tuple_conf = service.get_config(view="Full")
      print "service config:", tuple_conf[0]
      #for t in tuple_conf:
      #  print "\n tuple:", t
      search(tuple_conf[0])
      list_rcg = service.get_all_role_config_groups()
      print "role config groups:", list_rcg  
      for rcg in list_rcg:
        print "rcg:",rcg, " rcg config:", rcg.get_config(view="Full")
        rcg_dict = rcg.get_config(view="Full")
        search(rcg_dict)    
        list_roles = rcg.get_all_roles()
        print "list_roles:", list_roles
        for r in list_roles:
          r_dict = r.get_config(view="Full")
          print "role:", r, " config:", r_dict
          search(r_dict)



def args_parser():
  """
  """
  parser = argparse.ArgumentParser()
  parser.add_argument("--master_node", default='r2371-d5-us01', help='enter address of NameNode/HBase Master Node')  
  parser.add_argument("--cm_user", default='admin', help='Cloudera Manager user name, default is admin')
  parser.add_argument('--cm-password', default='admin', help='')



def main():
  """ 
  """
  api=ApiResource('r2341-d5-us01',username='admin')
  get_info(api)

if __name__=="__main__":
  main()
