#/usr/bin/env python

from cm_api.api_client import ApiResource,ApiException

#test how to create cluster; error condition if empty


def main():
  api = ApiResource(host='r2341-d5-us01',user='admin',password='admin')
  #is get cluster None? 
  what = api.get_all_clusters()
  print "what:", what

if __name__ == '__main__':
  main()
