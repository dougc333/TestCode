#!/usr/bin/env python



import sys
import argparse
from cm_api.api_client import ApiResource
from cm_api.api_client import ApiException



def checkServices(api):
  cluster = api.get_cluster("HDDTest")
  service_types = cluster.get_service_types()
  print "service_types:", service_types
  all_services = cluster.get_all_services(view="Full")
  print "all services:", all_services 
  host_templates = cluster.get_all_host_templates()
  print "host_templates:", host_templates 
  dashboard = api.get_dashboards()
  print "dashboard objects:", dashboard


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
   checkServices(api)

if __name__=='__main__':
  main()
  


