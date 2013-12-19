#!/bin/sh
iostat=`which iostat 2>/dev/null`
bc=`which bc 2>/dev/null`
function help {
echo -e "This plugin shows the I/O usage_rate of the specified disk, using the iostat external program.nt example nt ./io -d sda2 -w 10 -c 20"
        exit -1
}
# Ensuring we have the needed tools:
( [ ! -f $iostat ] ) && ( echo "ERROR: iostat command not found .Please install" && exit -1 )
# Getting parameters:
while getopts "d:w:c:h" OPT; do
        case $OPT in
                "d") disk=$OPTARG;;
                "w") warning=$OPTARG;;
                "c") critical=$OPTARG;;
                "h") help;;
        esac
done
# Adjusting the three warn and crit levels:
crit_util=`echo $critical`
warn_util=`echo $warning`
# Checking parameters:
[ ! -b "/dev/$disk" ] && echo "ERROR: Device incorrectly specified" && help
( [ $warn_util == "" ] || [ $crit_util == "" ] ) && echo "ERROR: You must specify all warning and critical levels" && help
( [[ "$warn_util" -ge  "$crit_util" ]] ) && echo "ERROR: critical levels must be highter than warning levels" && help
# Doing the actual check:
util=`$iostat -dx 1 10 $disk | grep $disk | awk '{print $12}'|sort -nr | head -n 1 `
# Comparing the result and setting the correct level:
if ( echo ${util} ${crit_util}|awk '!($1>=$2){exit 1}' );then
        msg="CRITICAL"
        status=2
else if ( echo ${util} ${warn_util} |awk '!($1>=$2){exit 1}');then
                msg="WARNING"
                status=1
     else
        msg="OK"
        status=0
     fi
fi
# Printing the results:
echo "$msg - I/O stats util_rate=$util  "
# Bye!
exit $status
