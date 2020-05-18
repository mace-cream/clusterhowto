## Edit qemu qcow2 file
`/home/feng/qemu/debian-jessie/hda.qcow2` is the virtual disk of the qemu vm. You can actually mount this disk without
starting the vm. The following steps are necessary to do this:
```shell
cd /home/feng/qemu/debian-jessie/
sudo modprobe nbd
sudo qemu-nbd --connect=/dev/nbd0 ./hda.qcow2
fdisk /dev/nbd0 -l
sudo partx -a /dev/nbd0
sudo mount /dev/nbd0p1 /home/feng/mntpoint/
# the following commands revert to normal
sudo umount /home/feng/mntpoint/
sudo qemu-nbd --disconnect /dev/nbd0
sudo rmmod nbd
```
See [this gist](https://gist.github.com/shamil/62935d9b456a6f9877b5) for further detail.
