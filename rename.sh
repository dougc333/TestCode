#!/bin/bash

num=0
for f in *
do
 if [[ $f != *.txt ]];then
   #echo "$f"
   mv "$f" "$f.txt"
   num=$[num+1]
 fi
done
echo "num: $num"

