#!/bin/bash -p 

#careful to not put / after jmx
curl -i http://r2341-d5-us02:50075/jmx?qry=Hadoop:service=DataNode,name=DataNodeActivity-r2341-d5-us02.dssd.com-50010
