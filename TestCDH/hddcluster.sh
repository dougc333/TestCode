#!/usr/bin/env python

# test creating hdd cluster; hardcoded tehe mount points on /testdir and /testdir2

from cm_api.api_client import ApiResource, ApiException


def main():
  print 'create HDD cluster'
  api = ApiResource('r2341-d5-us01.dssd.com', 'admin', 'admin')
  api.create_cluster(name="HDDTest", version="CDH5")
  sleep(10)



if __name__=='__main__':
  main()
  
