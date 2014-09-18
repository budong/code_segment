#!/bin/bash
#Reference:http://www.gnu.org/software/parted/manual/html_mono/parted.html
#Just for initialize disk

DISK=('/dev/sdc' '/dev/sdd' '/dev/sde' '/dev/sdf' '/dev/sdg' '/dev/sdh' '/dev/sdi' '/dev/sdj' '/dev/sdk' '/dev/sdl' '/dev/sdm' '/dev/sdn')

#install parted
yum -y install parted

#parted ,formating and create the file system
parted_fun()
{
parted -s $1 mklabel gpt
parted -s $1 mkpart primary 0 4000.2G
#parted -s $1 mkpart primary 0% 100%
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
i=1
for disk in ${DISK[@]};do
    parted_fun $disk
    mount_run $disk $i
    let i++
done
mount -a
}

#=========start script===========
main
