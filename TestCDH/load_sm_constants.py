#!/usr/bin/env python



#add area for CM_HOST, hosts in cluster 
#fix rest of files to grab config/url from this dictionary

config_file='/etc/cloudera-scm-server/db.mgmt.properties'


database_config={}



def parse(line):
  if not(line.startswith("#")) and line!=None:
    print "processing:%s", line
    key_value=line.split('=')
    key = key_value[0]
    #print "key:%s" % key
    value = key_value[1].strip()
    return [key,value]


def main():
  print 'parsing /etc/cloudera-scm-agent/db.mgmt.properties'
  with open(config_file) as f:
    for line in f:
      list_key_value = parse(line)
      if list_key_value!=None:
        print "list_key_value:%s",list_key_value
        database_config[list_key_value[0]]=list_key_value[1]
      #database_config[list_key_value[0]]= list_key_value[1]
  print "database_config", database_config


if __name__=='__main__':
  main()
