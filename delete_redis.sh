#!/bin/bash
all=`/usr/local/redis/bin/redis-cli keys "*"`
retain='na'

echo `/usr/local/redis/bin/redis-cli keys "*"`
for m in $all
do 
    n=`echo $m|cut -c 1-2`
    if [ $n != $retain ];then
        /usr/local/redis/bin/redis-cli del $m
    fi
done
echo `/usr/local/redis/bin/redis-cli keys "*"`
