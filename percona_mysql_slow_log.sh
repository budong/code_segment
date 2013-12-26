#!/bin/sh
pt-query-digest --no-report --review h=172.16.228.202,D=slow_query_210,t=query_review,p=slow_query,u=slow_query  \
--history h=172.16.228.202,D=slow_query_210,t=query_history,p=slow_query,u=slow_query \
--filter=" \$event->{Bytes} = length(\$event->{arg}) and \$event->{hostname}=\"$HOSTNAME\"" /data/mysql_db/slow.log
