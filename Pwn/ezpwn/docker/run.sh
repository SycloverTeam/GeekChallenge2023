#!/bin/sh
# Your program should be placed in /home/ctf
# We use proot for isolating, make /home/ctf as root dir.
# Replace the "helloworld" with your filename
#cd /home/ctf && su ctf -c "/bin/qemu-mipsel-static -L /usr/mipsel-linux-gnu ./pwn"
chroot --userspec=1000:1000 /home/ctf ./pwn
