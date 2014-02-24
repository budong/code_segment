#!/bin/sh

NUM=0
DATE_TIME=`date  +%Y-%m-%d`

while [[ $NUM -lt 1 ]];do
    ((NUM++))
    echo $NUM
done
