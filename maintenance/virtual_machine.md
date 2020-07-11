## Edit qemu qcow2 file
This is needed to extract the linux kernel and boot temporary file system

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

## Compile QEMU source code
```
./configure --help
./configure --enable-gtk # the missing deps can be installed by apt ...
make install # needs sudo, use make -j28 to accelerate
```

## GUI Arm64
The following command is used to boot the debian buster system from the virtual disk
```
qemu-system-aarch64 -smp 2 -netdev user,id=mynet -device virtio-net-device,netdev=mynet \
-m 2G -M virt -cpu cortex-a72 -drive if=none,file=hdd01.qcow2,format=qcow2,id=hd0 \
-device virtio-blk-device,drive=hd0 -device VGA \
-kernel vmlinuz-4.19.0-9-arm64 -append 'root=/dev/vda2' -initrd initrd.img-4.19.0-9-arm64 \
-device virtio-scsi-device -device usb-ehci -device usb-kbd -device usb-mouse -usb
```
To install the system for the first time, first you need to download the iso file, for example
[debian-10.4.0-arm64-netinst.iso](https://mirrors.tuna.tsinghua.edu.cn/debian-cd/10.4.0/arm64/iso-cd/debian-10.4.0-arm64-netinst.iso).

The second step is to create a virtual disk file. The command to do this is `qemu-img create`. We recommend `qcow2` format.
```
qemu-img create -q qcow2 hdd0.qcow2 40G
```
Then using the following command to launch the installer:
```
qemu-system-aarch64 -M virt -m 2048 -cpu cortex-a72 -smp 2 \
-drive if=none,file=debian-10.4.0-arm64-netinst.iso,id=cdrom,media=cdrom \
-device virtio-scsi-device -device scsi-cd,drive=cdrom \
-drive if=none,file=hdd0.qcow2,id=hd0 -device virtio-blk-device,drive=hd0
```
