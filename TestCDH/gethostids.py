#!/usr/bin/env python

import inspect
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



hosts =	{
      	'r2341-d5-us01.dssd.com': '86de389a-7182-4017-bab1-888ea2cff999',
       	'r2341-d5-us02.dssd.com': '80366fcb-7a0a-448e-836e-d02e299e7975',
       	'r2341-d5-us03.dssd.com': '79af8cf4-18e5-4192-b44b-fe7baa8e87a2',
       	'r2341-d5-us04.dssd.com': '24b2bf04-e4f3-41b5-993c-0633f44b087c'
   }


def get_info(api):
  hosts = api.get_all_hosts(view="Full")
  for host in hosts:
     #print host.__dict__
     print host.hostname, host.hostId
     

def test():
   print hosts['r2341-d5-us01.dssd.com']


def main():
  """ 
  """
  api=ApiResource('r2341-d5-us01',username='admin')
  get_info(api)
  test()
if __name__=="__main__":
  main()
