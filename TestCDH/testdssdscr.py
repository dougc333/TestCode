#!/usr/bin/env python

import sys
import argparse
import subprocess
from cm_api.api_client import ApiResource,ApiException
from cm_api.endpoints.cms import ClouderaManager
from cm_api.endpoints.parcels import get_parcel

from time import sleep
import re
import time

#from config import HDD_hdfs_config


#add solr and spark repos in check, install other repos? 
#the code drop repos dont contain the hardcoded spark and solr repos, from remore parcel url have to distribute/activate the spark and solr repos
beta_repo=[
  'http://dssd-beta:dssd-beta@bits.cloudera.com/73a30662/cm560/redhat/6/x86_64/cm/',
  'http://dssd-beta:dssd-beta@bits.cloudera.com/73a30662/cdh560/parcels/5.6.0.2/',
  'http://r2341-d5-us48.dssd.com/parcels/dssd/'
]

code_drop_6_repo=[
  'http://dssd:dssd@bits.cloudera.com/c515c923/',
  'http://dssd:dssd@bits.cloudera.com/9d7343ba/',
  'http://r2341-d5-us48.dssd.com/parcels/dssd/'
]



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

#clean up , screwed up
def clean_parcel_repo(api):
  repo_config=api.get_cloudera_manager().get_config(view="Full")['REMOTE_PARCEL_REPO_URLS']
  cleanMe= [x for x in repo_config if  x not in code_drop_6_repo]
  print "cleanME:", cleanMe
  
# this is still broken..some UI prompt for repo to use? 
#or test this with beta
def check_parcel_repos(api):
  repo_config=api.get_cloudera_manager().get_config(view="Full")['REMOTE_PARCEL_REPO_URLS']
  print 'repo_config: ',repo_config
  # test for code drop 6 repo
  if set(code_drop_6_repo) < set(repo_config.split(',')):
    print 'repo code drop 6 in parcels'
  elif set(beta_repo) < set(repo_config):
    print 'beta repo currently loaded in parcels'
  else:
    print "no repos loaded"
    # if nothing loaded we load code drop 6 # HAVE TO CVHANGE this later
    api.get_cloudera_manager().update_config({'REMOTE_PARCEL_REPO_URLS':repo_config.join(code_drop_6_repo)})
    time.sleep(10)


def download_dist_activate_parcel(cluster,api,parcel):
  """
  input: parcel object, output: should see parcel activated under Cloudera Manager UI
  """
  print "Downloading %s", parcel.product+parcel.version
  cmd = parcel.start_download()
  while parcel.stage != "DOWNLOADED":
    sleep(5)
    print parcel.stage
    print("."),
    parcel=get_parcel(api, parcel.product, parcel.version, cluster.name)
  print "parcel downloaded", parcel.product+" ,version:" + parcel.version + "DOWNLOADED"


  cmd = parcel.start_distribution()
  print "Distributing"
  while parcel.stage != "DISTRIBUTED":
    sleep(5)
    print("."),
    sys.stdout.flush()
    parcel= get_parcel(api,parcel.product, parcel.version, cluster.name)
  print "parcel distributed" , parcel.product + ", version:", parcel.version + "DISTRIBUTED"

  cmd = parcel.activate()
  if cmd.success != True:
    print "activation failed!!!"
    exit(0)

  print "Activating"
  while parcel.stage != "ACTIVATED":
    sleep(5)
    print".",
    parcel = get_parcel(api, parcel.product, parcel.version, cluster.name)  
  print "parcel activated" , parcel.product + ", version:", parcel.version + "ACTIVATED"

 
def add_parcels(api):
   """
   """  
   cm = api.get_cloudera_manager()
   for cluster in api.get_all_clusters():
      # get and list all available parcels
      parcels_dict={}
      for p in cluster.get_all_parcels():
        print '\t' + p.product + p.version
        if str(p.product+p.version).startswith("DSSD5.6.0"):
          print "found DSSD 5.6.0"
          parcels_dict[p.product+p.version]=p 
        #if p.product.startswith("IMPALA"):
        #  print "found Impala"
        #  parcels_list.append(p) 
        if str(p.product+p.version).startswith("CDH5.6.0"):
          print "found CDH 5.6.0"
          parcels_dict[p.product+p.version]=p 
        if p.product.startswith("DSSD_SCR"):
          print "found DSSD_SCR"
          parcels_dict[p.product+p.version]=p 
      print "num parcels to distribute and activate:", len(parcels_dict) 
      print "parcels_dict before downloading CDH: ",parcels_dict
      
   
      distMe = parcels_dict.get('CDH5.6.0-1.cdh5.6.0.p0.70')
      print "found CDH first, we update this first:", distMe.product+" ,version:"+distMe.version
      download_dist_activate_parcel(cluster,api,distMe)      
      if cm.get_config()[u"DSSD_ENABLED"]:
        #download the other parcels in the dictionary minus the CDH one which should be updated
        del parcels_dict['CDH5.6.0-1.cdh5.6.0.p0.70']
        print "after removal you should see 2 parcels here:", parcels_dict
        print "we are only downloading the dssd parcels"
        for p in parcels_dict.keys():
          download_dist_activate_parcel(cluster,api,parcels_dict.get(p))
      
      # set vm.swappiness and thp
      # this part below does not work, run ./swappy.sh manually 
      #config_swap_and_thp() 
      # inspect hosts
      print "inspecting hosts",
      cmd = cm.inspect_hosts()
      while cmd.success == None:
        sleep(5)
        print ".",
        cmd=cmd.fetch()
      
      if (cmd.success != True):
        print "host inspection failed"
        exit(0)
      
      print "hosts successfully inspected!!!" + cmd.resultMessage
 
      


def cm_args_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument("--cm_host", default="r2341-d5-us01",help="cloudera manager host address")
  parser.add_argument("--cm-user", default="admin", help="cloudera manager user name, should be admin unless you changed it")
  parser.add_argument("--cm-password", default="admin", help="default is admin, unless you changed it")
  return parser

def clean(api):
  for cluster in api.get_all_clusters():
    list_hosts = cluster.list_hosts
    print "hosts:" #use this to add back when creating the cluster hostIds
    print list_hosts
    print "cluster:" + cluster.name + " ,cluster version:" + cluster.version
    for service in cluster.get_all_services():
       service.stop().wait()
       cluster.delete_service(service.name)
    #delete cloudera mgmt service
    cm = ClouderaManager(api)
    try:
      cm.delete_mgmt_service()
    except ApiException:
      print "mgmt service doesn't exist"
    api.delete_cluster(cluster.name)



def main():
  parser = cm_args_parser()
  args = parser.parse_args()
  print "connecting to host:" + args.cm_host + "..."
  api = ApiResource(args.cm_host, username=args.cm_user, password=args.cm_password)
  print "done....."

 
if __name__ == '__main__':
  main()
