cloudera question: how to add final tag in after value tag? 
\


Contains Cloudera Manager automation code
current status: both HDD and DSSD mode work. Have to fix the OOM configuration and iterate
through the error messages for Cloudera Manager 

Debugging Notes: 
  when configuring HDFS through the API, you have to create a configuraiton in the api which the cloudera manager will create the exact hdfs-site.xml and core-site.xml files you need
  there are lots of missing parameters in the excample code; incompete
  for example fs.default.FS is not included. 

  hard to correlate all settings in hdfs-site.xml and core-site.xml from Cloudera manager to role config groups

1) start w/empty cloudera manager ./addSM.py to install cloudera management service
2) initservices.py (distributes, activates parcels)
3) installservices.py (installs hdfs)

Contains Impala benchmark code
1) generate data on each datanode
2) copy into hDFS 
