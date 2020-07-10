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

## GUI Arm64

```
qemu-system-aarch64 -smp 2 -netdev user,id=mynet -device virtio-net-device,netdev=mynet -m 2G -M virt -cpu cortex-a72 -drive if=none,file=hdd01.qcow2,format=qcow2,id=hd0 -device virtio-blk-device,drive=hd0 -device VGA -kernel vmlinuz-4.19.0-9-arm64 -append 'root=/dev/vda2' -initrd initrd.img-4.19.0-9-arm64 -device virtio-scsi-device -device usb-ehci -device usb-kbd -device usb-mouse -usb
```