#!/bin/bash -p

#call this before making data in each datnode for impala benchmark
# the datanodes have to be in this file

datanodes=('r2341-d5-us02' 
           'r2341-d5-us03' 
           'r2341-d5-us04');


for nodes in ${datanodes[@]};do
    printf "copying directory to $nodes \n"
    scp -r /root/cdhautomation root@$nodes:/root 
done

#run the makedata data creation on each node
for nodes in ${datanodes[@]};do
   printf "mvn clean, compile in nodes"
   printf "nodes:$nodes\n"
   ssh $nodes "cd /root/cdhautomation; mvn clean compile"
done
