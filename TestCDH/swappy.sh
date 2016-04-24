#!/bin/bash -p

#set swappiness using sysctl vm.swappiness=0
#dont change the /etc/sysctl.conf file; will mess up others
ssh root@r2341-d5-us01 "sysctl vm.swappiness=0"
ssh root@r2341-d5-us02 "sysctl vm.swappiness=0"
ssh root@r2341-d5-us03 "sysctl vm.swappiness=0"
ssh root@r2341-d5-us04 "sysctl vm.swappiness=0"

#ssh root@r2341-d5-us01 "echo never > /sys/kernel/mm/redhat_transparent_hugepage/defrag"
#ssh root@r2341-d5-us02 "echo never > /sys/kernel/mm/redhat_transparent_hugepage/defrag"
#ssh root@r2341-d5-us03 "echo never > /sys/kernel/mm/redhat_transparent_hugepage/defrag"
#ssh root@r2341-d5-us04 "echo never > /sys/kernel/mm/redhat_transparent_hugepage/defrag"
