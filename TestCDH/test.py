#!/usr/bin/env python

from cm_api.api_client import ApiResource, ApiException

def main():
  api = ApiResource('r2341-d5-us01',username='admin',password='admin')
  clusters = api.get_all_clusters()
  print "clusters:", clusters
  if len(clusters) == 0: 
    print "none"

if __name__ == '__main__':
  main()
