#!/usr/bin/env python

#adds HDFS
#install services; print out role config groups, fix customization for each RCG
#redo w/install services

import sys
import argparse
from cm_api.api_client import ApiResource,ApiException
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

from testdssdscr import add_hosts,add_parcels, check_parcel_repos,clean_parcel_repo



def createCluster(api):
  """
  creates either HDDTest or DSSDTest; should see this in Cloudera Manager UI
  """
  if len (api.get_all_clusters()) == 0:
     print "creating cluster"
     cm = api.get_cloudera_manager()
     if (cm.get_config().get(u"DSSD_ENABLED") == "true"):
       api.create_cluster("DSSDTest",version = "CDH5")
     else:
       api.create_cluster("HDDTest", version="CDH5")
   
  

def cm_args_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument("--cm_host",default="r2341-d5-us01", help="")
  parser.add_argument("--cm_user",default="admin",help="")
  parser.add_argument("--cm_password",default="admin",help="")
  return parser

def main():
   print "test services in cluster"
   parser = cm_args_parser()
   args = parser.parse_args()
   print "connecting to host:" +args.cm_host + "..."
   api = ApiResource(args.cm_host, username=args.cm_user, password = args.cm_password)
   print "done...."
   createCluster(api)
   #clean_parcel_repo(api)
   #check_parcel_repos(api)
   add_hosts(api)
   add_parcels(api)


if __name__=='__main__':
  main()
    


