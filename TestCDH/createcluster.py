#!/usr/bin/env python



#assumes DSSD Enabled set or not set 
#if DSSD Enabled set, will create DSSDTest cluster with SCR enabled
#if DSSD Enabled not set will create HDD cluster with SCR enabled


import cm_api.api_client import ApiResource, ApiException



def add_hosts(api):
   """
   This function assumes addSM has been run and the cluster exists
   This function assumes
   """
   for cluster in api.get_all_clusters():
      host_list = api.get_all_hosts(view="full")
      print host_list.to_json_dict(preserve_ro=True)
      hostId_list = []
      print "cluster name:%s", cluster.name + " cluster version:%s", cluster.version
      for i in range(0,len(host_list)):
          print "hostId[i]:"+host_list.to_json_dict(preserve_ro=True)["items"][i]["hostId"]
          hostId_list.append(host_list.to_json_dict(preserve_ro=True)["items"][i]["hostId"])
      cluster.add_hosts(hostId_list)




def main():
  print "creating cluster"
  


if __name__="__main__":
  main()
