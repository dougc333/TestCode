#!/bin/bash -p 

#careful to not put / after jmx
curl -i http://r2341-d5-us01:50070/jmx?qry=Hadoop:service=NameNode,name=NameNodeStatus
