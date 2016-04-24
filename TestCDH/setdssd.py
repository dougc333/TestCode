#!/usr/bin/env python

import argparse
import subprocess

from cm_api.api_client import ApiResource
from cm_api.endpoints.clusters import ApiCluster
from cm_api.endpoints.clusters import create_cluster
from cm_api.endpoints.parcels import ApiParcel
from cm_api.endpoints.parcels import get_parcel
from cm_api.endpoints.cms import ClouderaManager
from cm_api.endpoints.services import ApiService, ApiServiceSetupInfo
from cm_api.endpoints.services import create_service

from cm_api.api_client import ApiResource
from cm_api.api_client import ApiException
from cm_api.endpoints.clusters import create_cluster
from cm_api.endpoints.clusters import delete_cluster
from cm_api.endpoints.cms import ClouderaManager
from cm_api.endpoints.parcels import get_parcel


def cm_args_parser():
  parser=argparse.ArgumentParser()
  parser.add_argument("--cm_host",default='r2341-d5-us01',help='host name')
  parser.add_argument("--cm_user",default='admin',help='cloudera manager login user name')
  parser.add_argument("--cm_password",default='admin',help='cloudera manager login user password')
  return parser

def main():
  parser = cm_args_parser()
  args = parser.parse_args()
  print "conencting to host:",args.cm_host+"..."
  api = ApiResource(args.cm_host, username=args.cm_user, password=args.cm_password)
  cm = ClouderaManager(api)
  cm.update_config({"dssd_enabled":"true"})  

if __name__=="__main__":
  main()
