Title: Bluetooth Programming in Raspberry Pi
Date: 2018-03-13

[Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) comes with added wireless LAN and Bluetooth connectiviy. We can use [PyBluez](https://pybluez.github.io/) library to program Bluetooth in Python.

In order to install PyBluez, we first need to install Bluetooth development. In Raspberry Pi, run the `apt` command:

```
$ sudo apt install libbluetooth-dev
```

Then install PyBluez using `pip`:

```
$ pip install PyBluez
```

I am going to use Bluetooth RFCOMM to communicate with a mobile app. So I need to set up SPP (Serial Port Profile) in Raspberry Pi. But there is an issue with Bluez 5 in Raspberry Pi. To fix it, do the following:

```
$ sudo vi /etc/systemd/system/dbus-org.bluez.service
```

And add the following lines:

```
ExecStart=/usr/lib/bluetooth/bluetoothd -C
ExecStartPost=/usr/bin/sdptool add SP
ExecStartPost=/bin/chmod 777 /var/run/sdp
ExecStartPost=/bin/hciconfig hci0 piscan
```

The modified `dbus-org.bluez.service` is like this:

```
[Unit]
Description=Bluetooth service
Documentation=man:bluetoothd(8)
ConditionPathIsDirectory=/sys/class/bluetooth

[Service]
Type=dbus
BusName=org.bluez
ExecStart=/usr/lib/bluetooth/bluetoothd -C
ExecStartPost=/usr/bin/sdptool add SP
ExecStartPost=/bin/chmod 777 /var/run/sdp
ExecStartPost=/bin/hciconfig hci0 piscan
NotifyAccess=main
#WatchdogSec=10
#Restart=on-failure
CapabilityBoundingSet=CAP_NET_ADMIN CAP_NET_BIND_SERVICE
LimitNPROC=1
ProtectHome=true
ProtectSystem=full

[Install]
WantedBy=bluetooth.target
Alias=dbus-org.bluez.service
```

Then reboot Raspberry Pi.