#!/bin/bash -p

# we need this before NN format for starting dssd datanode hdfs 
# 

rm -rf /testdir/dfs
rm -rf /testdir2/dfs
rm -rf /tmp/hadoop-hdfs
rm -rf /var/run/hdfs-sockets
ssh root@r2341-d5-us32 "rm -rf /testdir/dfs"
ssh root@r2341-d5-us32 "rm -rf /testdir2/dfs"
ssh root@r2341-d5-us32 "rm -rf /tmp/hadoop-hdfs"
ssh root@r2341-d5-us32 "rm -rf /dfs/dn"
ssh root@r2341-d5-us32 "rm -rf /var/run/hdfs-sockets"
ssh root@r2341-d5-us33 "rm -rf /testdir/dfs"
ssh root@r2341-d5-us33 "rm -rf /testdir2/dfs"
ssh root@r2341-d5-us33 "rm -rf /tmp/hadoop-hdfs"
ssh root@r2341-d5-us33 "rm -rf /dfs/dn"
ssh root@r2341-d5-us33 "rm -rf /var/run/hdfs-sockets"
ssh root@r2341-d5-us34 "rm -rf /testdir/dfs"
ssh root@r2341-d5-us34 "rm -rf /testdir2/dfs"
ssh root@r2341-d5-us34 "rm -rf /tmp/hadoop-hdfs"
ssh root@r2341-d5-us34 "rm -rf /dfs/dn"
ssh root@r2341-d5-us34 "rm -rf /var/run/hdfs-sockets"

