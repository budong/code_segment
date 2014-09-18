#!/bin/bash
#Just for initialize disk

DISK=('/dev/sdb' '/dev/sdc' '/dev/sdd' '/dev/sde' '/dev/sdf' '/dev/sdg' '/dev/sdh' '/dev/sdi' '/dev/sdj' '/dev/sdk' '/dev/sdl' '/dev/sdm' '/dev/sdn')

#fdisk ,formating and create the file system
fdisk_fun()
{
fdisk -S 56 $1 << EOF
n
p
1


wq
EOF

sleep 5
mkfs.ext4 ${1}1
}

#config /etc/fstab and mount device
mount_run()
{
mkdir -p /data$2
uuid=`/sbin/blkid ${1}1|awk '{print $2}'`
echo "$uuid             /data$2                 ext4    defaults        0 0" >> /etc/fstab
}

#initialize...
main()
{
i=0
for disk in ${DISK[@]};do
    fdisk_fun $disk
    mount_run $disk $i
    let i++
done
mount -a
}

#=========start script===========
main

