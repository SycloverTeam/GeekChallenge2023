#!/bin/sh
# container startup script
# DO NOT EDIT
echo $geek_flag>/home/ctf/flag
export FLAG=''
FLAG=''
/busybox nc -lkp 2333 -v -e /run.sh
#sleep infinity;
